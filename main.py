from typing import Tuple, Optional, Literal, Any
from pydantic import BaseModel, Field, model_validator, field_validator
from litellm import completion
import instructor
from dotenv import load_dotenv
import orjson
import pathlib

load_dotenv()

with (
    pathlib.Path("data/engines.json").open("r", encoding="utf-8") as json_file,
    pathlib.Path("data/engines.md").open("r", encoding="utf-8") as md_file,
    pathlib.Path("data/system_instructions.md").open(
        "r", encoding="utf-8"
    ) as system_instructions_file,
):
    engines_json = orjson.loads(json_file.read())
    engines_md = md_file.read()
    system_instructions = system_instructions_file.read()


class QueryModel(BaseModel):
    selected_engine: Literal[*engines_json["engines"].keys()] = Field(
        ...,
        description=f"The search engine to use. Must be either from: ({', '.join(engines_json['engines'].keys())})",
    )
    query_modify: Tuple[bool, Optional[str]] = Field(
        ...,
        description=(
            "A tuple of (bool, Optional[str]). If the bool is True, the str is the query to modify. If the bool is False, the str is ignored."
        ),
    )

    @field_validator("query_modify", mode="before")
    @classmethod
    def normalize(cls, v: Any) -> Tuple[bool, Optional[str]]:
        # Convert list to tuple if needed
        if isinstance(v, list):
            v = tuple(v)

        match v:
            case bool() as b:
                return (b, None)
            case str() as s:
                return (True, s)
            case (str() as s,):
                return (True, s)
            case (bool() as b,):
                return (b, None)
            case tuple() as t:
                return t
            case _:
                return v

    @model_validator(mode="after")
    def validate(self):
        if self.query_modify:
            first, second = self.query_modify
            match (first, second):
                case (True, None):
                    raise ValueError(
                        "Second element of query_modify must be provided if first is True."
                    )
                case (False, _):
                    self.query_modify = (False, None)
        return self


client = instructor.from_litellm(completion)
original_query = "how does an llm works use perplexity"

response = client.chat.completions.create(
    model="groq/llama-3.3-70b-versatile",
    messages=[
        {
            "role": "system",
            "content": system_instructions,
        },
        {
            "role": "user",
            "content": [
                {"type": "text", "text": f"USER QUERY\n{original_query}"},
                {"type": "text", "text": f"ENGINE DATA\n{engines_md}"},
            ],
        },
    ],
    response_model=QueryModel,
    temperature=0,
    max_retries=5,
)

selected_engine = response.selected_engine
query_modify = response.query_modify

query = query_modify[1] if query_modify[0] else original_query

engine_url = engines_json["engines"][selected_engine]["engine_url"]
search_url = engine_url.replace("%s", query).replace(" ", "%20")

print(search_url)

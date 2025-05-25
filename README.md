# aRouter: Intelligent Search Engine Router

aRouter is an intelligent search engine router that uses large language models (LLMs) to analyze search queries and automatically select the most appropriate search engine. It can also optimize queries for the selected engine to improve search results.

## ✨ Features

- **Smart Engine Selection**: Automatically routes queries to the most suitable search engine based on the query's intent and content
- **Query Optimization**: Optionally refines search queries to improve result quality
- **Customizable Engine List**: Easily configure your preferred search engines with custom priorities
- **Privacy-Focused**: No tracking or logging of searches
- **Extensible**: Simple JSON configuration for adding or modifying search engines

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/aRouter.git
   cd aRouter
   ```

2. Install dependencies using `uv` (recommended):
   ```bash
   uv add instructor litellm orjson pydantic python-dotenv
   ```

   Or using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file with your API keys (if needed for specific engines):
   ```env
   OPENAI_API_KEY=your_openai_api_key
   ```

## 🛠️ Configuration

aRouter is configured using JSON files in the `data` directory:

### `engines.json`

This file defines the available search engines and their properties. Example structure:

```json
{
  "meta_user_notes": "Search engines configuration with detailed descriptions and settings. Priority levels: high (frequently used), medium (general purpose), low (specialized).",
  "engines": {
    "google_search": {
      "description": "Google Search is a versatile, general-purpose search engine suitable for a wide range of queries...",
      "engine_url": "https://www.google.com/search?q=%s",
      "query_modifiable": true,
      "supports_search_operator": true,
      "user_notes": null,
      "priority": "high"
    },
    "perplexity": {
      "description": "AI-powered search engine that provides direct, well-sourced answers to questions...",
      "engine_url": "https://www.perplexity.ai/search?q=%s",
      "query_modifiable": true,
      "supports_search_operator": true,
      "user_notes": "Free tier available with daily limits",
      "priority": "medium"
    }
  }
}
```

### Engine Properties

- `description`: Detailed description of the engine's capabilities (used by the LLM to select the engine)
- `engine_url`: The search URL with `%s` as the query placeholder
- `query_modifiable`: Whether the query can be optimized for this engine
- `supports_search_operator`: Whether the engine supports advanced search operators
- `user_notes`: Optional notes about the engine
- `priority`: User-defined priority (high/medium/low) for engine selection

## 🚀 Usage

Run the router with a search query:

```bash
python main.py
```

### Example

```python
original_query = "capital of france"

# The router will:
# 1. Analyze the query
# 2. Select the most appropriate search engine
# 3. Optionally optimize the query
# 4. Return the final search URL
```

## 🤖 How It Works

1. **Query Analysis**: The LLM analyzes the search query to understand its intent and requirements.
2. **Engine Selection**: Based on the query and configured engines, the most suitable search engine is selected.
3. **Query Optimization**: If enabled, the query may be refined to improve search results.
4. **URL Generation**: The final search URL is generated and returned.

## 📚 Supported Search Engines

aRouter supports a wide variety of search engines including:

- Google Search
- Bing
- DuckDuckGo
- Perplexity AI
- Brave Search
- Wikipedia
- And more...

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Operation Logic
1. First, there is an engines.json that contains information about engines and user preferences. It is in this format:
```json
{
	"meta_user_notes": null,
	"engines": {
		"google_search": {
			"description": "Google Search is a versatile, general-purpose search engine suitable for a wide range of queries, from simple facts to complex research. It provides comprehensive results, including web pages, images, news, and scholarly articles. Ideal for broad searches, local information, or when diverse result types are needed. Supports advanced search operators (e.g., quotes, -, +) for precise query refinement.",
			"engine_url": "https://www.google.com/search?q=%s",
			"query_modifiable": true,
			"supports_search_operator": true,
			"user_notes": null,
			"priority": "medium"
		},
		"perplexity": {
			"description": "Perplexity is an AI-powered search engine designed for direct, concise answers to specific questions. It leverages natural language processing to provide summarized responses with source citations, making it ideal for factual queries, quick insights, or when users prefer brief, synthesized information over extensive web results. Supports query reformulation for clarity and focus.",
			"engine_url": "https://www.perplexity.ai/search?q=%s",
			"query_modifiable": true,
			"supports_search_operator": true,
			"user_notes": null,
			"priority": "medium"
		}
	}
}
```

In here, we have:
- Meta User Notes: The user's general notes about all the engines like their preferences, requirements, special instructions, etc.
- Engines: The engines that are available. Each engine has:
    - Description: A detailed description of the engine, this is what LLMs use to understand the engine and it's capabilities.
    - Engine URL: The URL of the engine. %s will be replaced with the query. The LLM will don't see this.
    - Extra: Extra information about the engine. It is a dictionary that contains:
        - Query Changeable: Whether the query can be changed by the LLM or not.
        - Supports Search Operator: Whether the engine supports search operators or not. (Like advanced search operators in Google +, -, quote, filetype etc.)
        - User Notes: The user's notes about this specific engine.
        - Priority: The priority of the engine. It can be high, medium, or low. The LLM will use this to determine which engine to use. This is user's priority, not the LLM's.

**After this JSON is created, the logic will convert it to a LLM-friendly format and use it to determine which engine to use.**

It becomes something like this:
```md
# Meta User Notes: None
## Engines
### google_search
Google Search is a versatile, general-purpose search engine suitable for a wide range of queries, from simple facts to complex research. It provides comprehensive results, including web pages, images, news, and scholarly articles. Ideal for broad searches, local information, or when diverse result types are needed. Supports advanced search operators (e.g., quotes, -, +) for precise query refinement.
- Query Modifiable: True
- Supports Search Operator: True
- User Notes: None
- Priority: medium

### perplexity
Perplexity is an AI-powered search engine designed for direct, concise answers to specific questions. It leverages natural language processing to provide summarized responses with source citations, making it ideal for factual queries, quick insights, or when users prefer brief, synthesized information over extensive web results. Supports query reformulation for clarity and focus.
- Query Modifiable: True
- Supports Search Operator: True
- User Notes: None
- Priority: medium
```

2. Then, we have a very strict and versatile Pydantic model that represent, harden and validate the upcoming LLM output correctly.

```python
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
```

After this, we have a LLM that will generate the output. To instruct the LLM, we use the engines.md and system_instructions.md files.

At the end, we can route the query to the selected engine.

# TODO
- [ ] Make extension
- [ ] Make this README more detailed
- [ ] Implement something like auto-fill superfast completion
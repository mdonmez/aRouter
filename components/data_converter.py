"""
This script will get the engines.json file and convert it to a markdown file with special formatting that suitable for most LLMs.
This script should be run every time the engines.json file is updated. NOT every time the program is run.
"""

import orjson
import time


def convert(json_path: str, md_path: str):
    start_time = time.perf_counter()
    with open(json_path, "rb") as f:
        json_data = orjson.loads(f.read())

    with open(md_path, "w") as f:
        f.write("# Meta User Notes: None\n")
        f.write("## Engines\n")
        for engine_name, engine_data in json_data["engines"].items():
            f.write(f"### {engine_name}\n")
            f.write(f"{engine_data['description']}\n")
            f.write(f"- Query Modifiable: {engine_data['query_modifiable']}\n")
            f.write(
                f"- Supports Search Operator: {engine_data['supports_search_operator']}\n"
            )
            f.write(f"- User Notes: {engine_data['user_notes']}\n")
            f.write(f"- Priority: {engine_data['priority']}\n")
            f.write("\n")
    end_time = time.perf_counter()
    print(f"Conversion completed in {end_time - start_time:.6f} seconds")


if __name__ == "__main__":
    convert("data/engines.json", "data/engines.md")

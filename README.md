# aRouter

Fully automated router that can be easily applied to any search system to optimize the query using LLMs and redirect it to the right engine.

## Usage Purposes
- Browser search engines
- Any other search system that contains more than one search engine

## Operation Logic
1. First, there is an engines.json that contains information about engines and user preferences. It is in this format:
```json
{
	"meta_user_notes": "None",
	"engines": {
		"google_search": {
			"description": "Google Search is a versatile, general-purpose search engine suitable for a wide range of queries, from simple facts to complex research. It provides comprehensive results, including web pages, images, news, and scholarly articles. Ideal for broad searches, local information, or when diverse result types are needed. Supports advanced search operators (e.g., quotes, -, +) for precise query refinement.",
			"engine_url": "https://www.google.com/search?q=%s",
			"extra": {
				"query_changeable": true,
				"supports_search_operator": true,
				"user_notes": "None",
				"priority": "medium"
			}
		},
		"perplexity": {
			"description": "Perplexity is an AI-powered search engine designed for direct, concise answers to specific questions. It leverages natural language processing to provide summarized responses with source citations, making it ideal for factual queries, quick insights, or when users prefer brief, synthesized information over extensive web results. Supports query reformulation for clarity and focus.",
			"engine_url": "https://www.perplexity.ai/search?q=%s",
			"extra": {
				"query_changeable": true,
				"supports_search_operator": true,
				"user_notes": "None",
				"priority": "high"
			}
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
# Meta User Notes
None

## Engines

### google_search
- Description: Google Search is a versatile, general-purpose search engine suitable for a wide range of queries, from simple facts to complex research. It provides comprehensive results, including web pages, images, news, and scholarly articles. Ideal for broad searches, local information, or when diverse result types are needed. Supports advanced search operators (e.g., quotes, -, +) for precise query refinement.
- Query Changeable: True
- Supports Search Operator: True
- User Notes: None
- Priority: medium

### perplexity
- Description: Perplexity is an AI-powered search engine designed for direct, concise answers to specific questions. It leverages natural language processing to provide summarized responses with source citations, making it ideal for factual queries, quick insights, or when users prefer brief, synthesized information over extensive web results. Supports query reformulation for clarity and focus.
- Query Changeable: True
- Supports Search Operator: True
- User Notes: None
- Priority: high
```

2. Then, we have a Pydantic model that represent, harden and validate the upcoming LLM output correctly.

```python
class EngineSelection(BaseModel):
    meta_user_notes: str
    engines: Dict[str, Engine]
```

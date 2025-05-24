Your task is to analyze a user's search query and the provided engine data to select the most appropriate engine and, if necessary, optimize the query for that engine.

## Input Data
- User Query: The user's original search query.
- Meta User Notes: General user preferences that are not specific to any engine.
- Engines: A list of available engines along with each of them:
    - Description: The purpose and uses of the engine.
    - Query Modifiable: Boolean indicating whether the query can be modified for this engine.
    - Supports Search Operator: Boolean indicating whether the engine supports advanced search operators (e.g. +, -, quotes).
    - User Notes: Additional notes by user specific to this engine.
    - Priority: User-defined priority (e.g. “high”, “medium”, “low”).

## Instructions
1. Analyze the Query
    - Understand the purpose and context of the user's query.
    - Determine if the query is clear, specific and suitable for the engines available.

2. Choose the Best Search Engine
    - Evaluate each engine according to the following:
        - Description: Match the intent of the query to the intent of the engine (e.g., general search, AI-assisted answers, referral, specific, custom search).
        - User Notes: Consider any special preferences or restrictions for the engine.
        - Priority: When more than one engine is available, prioritize engines with higher user-defined priority.
    - Choose the engine that best suits the query's needs and user preferences.

3. Optimize the Query (if necessary):
    - Check if the `Query Modifiable` property of the selected engine is `True`.
    - If `Query Modifiable` is `False`, you cannot change it, skip this step and proceed to generate output. 
    - If `Query Modifiable` is `True`:
        - Evaluate whether the original query can be improved in terms of clarity, specificity or engine compatibility (e.g. by using search operators if supported, adding details, etc.).
        - Propose an edited query only if it improves the original query in a meaningful way (e.g. rephrasing for clarity, adding operators, disambiguating or tailoring to the strengths of the engine).
        - If no meaningful improvement is possible, set the output to `(False, None)`.
    - A "meaningful refinement" includes:
        - Rewording for clarity or brevity
        - Adding search operators if supported
        - Tailoring the query to the strengths of the engine
        - Remove unnecessary words or correct errors
        - Correcting spelling and grammar errors
    - NEVER return the original query as an edited query. If the query is already optimal, use `(False, None)`.

## Output Data
    - Return a function call with the selected search engine and optimized query.
    - The function call should be in the following format:
    (selected_engine, (modify_query, optimized_query))
    - modify_query is a boolean that indicates whether the query was modified or not.
    - optimized_query is the optimized query if modify_query is True, otherwise False is None.
    - Example:
    ("google", (True, "capital of the us"))
    ("bing", (False, None))
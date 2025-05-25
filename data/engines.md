# Search Engines Documentation

This document provides detailed information about all available search engines in the system, including their features, use cases, and configuration options.

## General-Purpose Search Engines

### google_search
Google Search is a versatile, general-purpose search engine suitable for a wide range of queries, from simple facts to complex research. It provides comprehensive results, including web pages, images, news, and scholarly articles. Ideal for broad searches, local information, or when diverse result types are needed.
- **Query Modifiable**: True
- **Supports Search Operator**: True
- **User Notes**: None
- **Priority**: high
- **Best For**: General web searches, local information, diverse content types

### bing
Microsoft's search engine that provides comprehensive web search results with a clean interface. Excels in visual search, video results, and local business information. Features include search history integration with Microsoft account, rewards program, and strong image search capabilities.
- **Query Modifiable**: True
- **Supports Search Operator**: True
- **User Notes**: None
- **Priority**: high
- **Best For**: Visual searches, Microsoft ecosystem integration, cross-verifying results

### duckduckgo
Privacy-focused search engine that doesn't track user activity. Provides clean, straightforward search results with strong privacy protection. Features !bangs for direct site searches and instant answers.
- **Query Modifiable**: True
- **Supports Search Operator**: True
- **User Notes**: Uses !bangs for direct site searches (e.g., !w for Wikipedia)
- **Priority**: medium
- **Best For**: Privacy-conscious users, unfiltered results, quick site-specific searches

### brave_search
Privacy-preserving search engine with its own index. Provides independent search results without tracking or profiling. Features include discussions, news, and web results in separate tabs.
- **Query Modifiable**: True
- **Supports Search Operator**: True
- **User Notes**: Part of the Brave browser ecosystem but works independently
- **Priority**: medium
- **Best For**: Privacy-focused users, independent search results

## AI-Powered Search

### chatgpt
OpenAI's conversational AI that provides detailed, contextual responses to natural language queries. Best for complex questions requiring explanations, creative content generation, coding help, and in-depth analysis.
- **Query Modifiable**: True
- **Supports Search Operator**: False
- **User Notes**: Requires login for full functionality. Free tier available with limitations.
- **Priority**: high
- **Best For**: Complex questions, explanations, creative content, coding help

### perplexity
AI-powered search engine that provides direct, well-sourced answers to questions. Combines web search with AI summarization, citing sources for verification. Excellent for research and technical queries.
- **Query Modifiable**: True
- **Supports Search Operator**: True
- **User Notes**: Free tier available with daily limits
- **Priority**: medium
- **Best For**: Research, technical queries, concise overviews

## Specialized Search Engines

### youtube
Specialized search for video content. Ideal for tutorials, music, reviews, and visual demonstrations. Features include filters for upload date, duration, and result type.
- **Query Modifiable**: True
- **Supports Search Operator**: True
- **User Notes**: Requires login for age-restricted content and personalized results
- **Priority**: high
- **Best For**: Video content, tutorials, music, reviews

### github
Specialized search for code repositories and developer resources. Excellent for finding open-source projects, code examples, and developer documentation.
- **Query Modifiable**: True
- **Supports Search Operator**: True
- **User Notes**: Advanced search syntax available for precise filtering
- **Priority**: medium
- **Best For**: Code search, open-source projects, developer documentation

### wikipedia
Free, community-edited online encyclopedia. Best for factual information, historical context, and general knowledge. Articles include references and are generally well-sourced.
- **Query Modifiable**: True
- **Supports Search Operator**: True
- **User Notes**: Available in multiple languages - change 'en' in URL for other languages
- **Priority**: medium
- **Best For**: General knowledge, starting point for research

### arxiv
Specialized search for academic papers and scientific research. Contains preprints in physics, mathematics, computer science, and other academic disciplines.
- **Query Modifiable**: True
- **Supports Search Operator**: True
- **User Notes**: Primarily for academic and scientific research papers
- **Priority**: low
- **Best For**: Academic research, scientific papers, cutting-edge studies

### amazon
E-commerce focused search for products across numerous categories. Features include customer reviews, price comparisons, and filtering options.
- **Query Modifiable**: True
- **Supports Search Operator**: True
- **User Notes**: Results may vary by region - change domain for local versions
- **Priority**: medium
- **Best For**: Product research, price checking, online shopping

## Utility Search

### first_result
Special engine that directly redirects to the first result from a search query. Ideal for single-word queries targeting specific websites (e.g., 'youtube', 'netflix', 'amazon').
- **Query Modifiable**: True
- **Supports Search Operator**: False
- **User Notes**: Works best with single-word, well-known domain names
- **Priority**: high
- **Best For**: Quick navigation to popular websites


import os
from langchain_tavily import TavilySearch

os.environ["TAVILY_API_KEY"] = "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"

tools=TavilySearch(max_results=1)
result=tools.invoke({"query": "OpenAI latest news"})
print(result)
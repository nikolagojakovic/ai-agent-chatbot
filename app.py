from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
#from langchain_community.tools.tavily_search import 
from dotenv import load_dotenv
load_dotenv()

import os
# Now use os.environ["TAVILY_API_KEY"] and os.environ["GROQ_API_KEY"]
groq_api_key = os.environ["GROQ_API_KEY"]
os.environ["TAVILY_API_KEY"] = os.environ["TAVILY_API_KEY"]

from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch




groq_api_key="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"


models=[
"llama3-70b-8192",
"mixtral-8x7b-32768"
]

tool_tavily=TavilySearch(max_results=2)

tools=[tool_tavily,]

app=FastAPI(title="LangGraph Groq Agent API",)


class Request(BaseModel):
    model_name: str
    system_prompt: str
    messages: List[str]


@app.post("/run_agent")


def chat_endpoint(request: Request):
    model_name = request.model_name
    system_prompt = request.system_prompt
    messages = request.messages

    if model_name not in models:
        return {"error": "Model not supported"}

    chat_model = ChatGroq(model_name=model_name, api_key=groq_api_key)
    
    agent = create_react_agent(
    model=chat_model,
    tools=tools,
    system_prompt=system_prompt,
    verbose=True,
)

    state={"messages": request.messages}

    
    response = agent.invoke(state)
    
    # Make sure to return messages in the expected format
    if isinstance(response, dict) and "messages" in response:
        return {"messages": response["messages"]}
    else:
        return {"error": "Agent did not return messages."}

    


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)




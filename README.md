This project is a FastAPI-powered backend and Streamlit frontend for interacting with advanced AI models and web search tools.

Features:

Chat with large language models (Groq’s Llama3 and Mixtral) via a simple API.
Integrates the TavilySearch tool for real-time web search within conversations.
Customizable system prompt for agent personality and instructions.
Streamlit UI for easy user interaction.
Secure API key management using a .env file.
How it works:

The FastAPI backend exposes a /run_agent endpoint that receives chat requests, selects the model, and invokes the agent.
The agent can use both the selected AI model and the TavilySearch tool to answer queries.
The Streamlit frontend lets users select a model, define the agent’s system prompt, and chat with the agent.
Responses are displayed in the UI, including results from web searches if triggered.
Setup:

Add your API keys to a .env file.
Start the FastAPI backend (python app.py).
Run the Streamlit frontend (streamlit run ui.py)

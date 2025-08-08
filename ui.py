import streamlit as st
import requests

st.set_page_config(page_title="AI Agent", page_icon=":robot_face:", layout="centered")


API_URL = "http://127.0.0.1:8000/run_agent"


models=[
"llama3-70b-8192",
"mixtral-8x7b-32768"
]

st.title("AI Agent Chat Interface")
st.write("Interact with the AI agent using the selected model.")

given_system_prompt = st.text_area("Define your Agent")


selected_model = st.selectbox("Select Model:", models)

user_input = st.text_area("Type your message here...", placeholder="Type your prompt here...")

if st.button("Submit"):
    if user_input.strip():
        try:
            # Send the input to the FastAPI backend
            payload = {"messages": [user_input], "model_name": selected_model, 'system_prompt': given_system_prompt}
            response = requests.post(API_URL, json=payload)

            # Display the response
            if response.status_code == 200:
                response_data = response.json()
                if "error" in response_data:
                    st.error(response_data["error"])
                else:
                    ai_responses = [
                        message.get("content", "")
                        for message in response_data.get("messages", [])
                        if message.get("type") == "ai"
                    ]

                    if ai_responses:
                        st.subheader("Agent Response:")
                        st.markdown(f"**Final Response:** {ai_responses[-1]}")
                        # for i, response_text in enumerate(ai_responses, 1):
                        #     st.markdown(f"**Response {i}:** {response_text}")
                    else:
                        st.warning("No AI response found in the agent output.")
            else:
                st.error(f"Request failed with status code {response.status_code}.")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a message before clicking 'Send Query'.")

        
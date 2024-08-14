from huggingface_hub import InferenceClient
import streamlit as st
from dotenv import load_dotenv
import os
import shelve

load_dotenv()

st.title("🤗💬 HugChat App")

USER_AVATAR = "😎"
BOT_AVATAR = "⚡"


client = InferenceClient(
    "mistralai/Mistral-7B-Instruct-v0.3",
    token=os.getenv("HUGGINGFACE_API_TOKEN")
)


if "hf_model" not in st.session_state:
    st.session_state["hf_model"] = "mistralai/Mistral-7B-Instruct-v0.3"


def load_chat_history():
    with shelve.open("chat_history") as db:
        return db.get("messages", [])



def save_chat_history(messages):
    with shelve.open("chat_history") as db:
        db["messages"] = messages



if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()


with st.sidebar:
    if st.button("Delete Chat History"):
        st.session_state.messages = []
        save_chat_history([])
    
    st.title('🤗💬 HugChat App')
    st.markdown('''
    ## About
    This app is an LLM-powered chatbot built🛠️ using:
    - [Streamlit](https://streamlit.io/)
    - [🤗Hugging Face](https://huggingface.co/)
    - [mistralai/Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3) LLM model
    
    
    ''')
    
    st.write('Made by Sidhartha Reddy' )


for message in st.session_state.messages:
    avatar = USER_AVATAR if message["role"] == "user" else BOT_AVATAR
    with st.chat_message(message["role"], avatar=avatar):
        st.markdown(message["content"])


if prompt := st.chat_input("How can I help?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=USER_AVATAR):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=BOT_AVATAR):
        message_placeholder = st.empty()
        full_response = ""
        for response in client.chat_completion(
            messages=st.session_state["messages"],
            max_tokens=500,
            stream=True,
        ):
            full_response += response.choices[0].delta.content or ""
            message_placeholder.markdown(full_response + "|")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})

save_chat_history(st.session_state.messages)

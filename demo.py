# author: AllByAI, TorusAI
# this software is licensed under the Toro-LlaMA License and Llama2.

import streamlit as st
from langchain.callbacks.base import BaseCallbackHandler
import openai

# you no need to change this since we are using self-host model
openai.api_key = "EMPTY"

# change to the host that model deployed using Fastchat
openai.api_base = "https://localhost/api/v1"

HISTORY_LEN = 5  # Maximum history length that chatbot can remember
PROMPT_SYSTEM = "Cuộc hội thoại giữa người dùng và một trí thông minh nhân tạo. Đưa ra câu trả lời chính xác, giúp ích cho người dùng."
GPT_MODEL = "allbyai/ToroLLaMA-7b-v1.0"


class ChatMessage():
    def __init__(self, role="user", message=""):
        """
            Properties:
                role: "user" or "assistant"
                message: the message
        """
        self.role = role
        self.message = message

    def __str__(self):
        return f"{self.message}"


class StreamHandler(BaseCallbackHandler):
    """Call back handler for streamlit stream output
    """

    def __init__(self, container, initial_text="", display_method='markdown'):
        self.container = container
        self.text = initial_text
        self.display_method = display_method

    def on_llm_new_token(self, token: str, **kwargs) -> None:
        self.text += token
        display_function = getattr(self.container, self.display_method, None)
        if display_function is not None:
            display_function(self.text)
        else:
            raise ValueError(f"Invalid display_method: {self.display_method}")


class QAModules:
    def __init__(self):
        self.qa_queue_len = HISTORY_LEN

    def get_chatbot_response(self, chat_session):
        """Get chatbot response with intention detection and knowledge base lookup

        Args:
            chat_session (ChatMessage[]): chat history
        Returns:
            str: Answer of LLM
        """
        chat_session = chat_session[-self.qa_queue_len:]

        chat_session_str = [{"role": "system", "content": PROMPT_SYSTEM}]
        # Exclude the last message
        for message in chat_session:
            chat_session_str.append(
                {"role": message.role, "content": str(message)})
        answer = openai.ChatCompletion.create(
            model=GPT_MODEL,
            messages=chat_session_str,
            temperature=0,
            presence_penalty=2,
            frequency_penalty=2,
            stream=True,
            stop_str=["</s>"]
        )
        for chunk in answer:
            if chunk["choices"][0]["finish_reason"] != "stop":
                if 'content' in chunk['choices'][0]['delta']:
                    yield chunk["choices"][0]["delta"]['content']
                else:
                    yield ""


@st.cache_resource
def get_qa_session():
    return QAModules()


client = get_qa_session()


def main():
    user_input = st.chat_input("You", key="user_input")
    st.title("Toro-LlaMA - power by allby.ai")
    item: ChatMessage
    for item in st.session_state.chatlog:
        if item.role == "user":
            with st.chat_message("User", avatar="🧑‍💻"):
                st.write(item.message)
        if item.role == "assistant":
            with st.chat_message("Assistant", avatar="💻"):
                st.write(item.message)
    if user_input:
        st.session_state.chatlog.append(ChatMessage("user", user_input))
        with st.chat_message("User", avatar="🧑‍💻"):
            st.write(user_input)

        with st.chat_message("Assistant", avatar="💻"):
            container = st.empty()

            stream_handler = StreamHandler(container)
            assistant_answer_stream = client.get_chatbot_response(
                st.session_state.chatlog)
            assistant_answer = ''
            for token in assistant_answer_stream:
                stream_handler.on_llm_new_token(token)
                assistant_answer += token
            st.session_state.chatlog.append(
                ChatMessage("assistant", assistant_answer))


if __name__ == "__main__":
    if "chatlog" not in st.session_state:
        st.session_state.chatlog = []
    st.markdown(
        """
        <style>
        button {
            height: auto;
            padding-top: 12px !important;
            padding-bottom: 12px !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    main()

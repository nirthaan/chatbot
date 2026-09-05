import os
import warnings

import streamlit as st
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langgraph.prebuilt import create_react_agent

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
load_dotenv()


@tool
def calculator(a: float, b: float) -> str:
    """Add two numbers."""
    return f"The sum of {a} and {b} is {a + b}"


@tool
def say_hello(name: str) -> str:
    """Greet a user."""
    return f"Hello {name}, I hope you are well today"


@st.cache_resource(show_spinner=False)
def create_agent():
    model_name = os.getenv("GROQ_MODEL", "qwen/qwen3.6-27b")
    model = ChatGroq(model=model_name, temperature=0)
    return create_react_agent(model, [calculator, say_hello])


def get_response(prompt: str) -> str:
    agent_executor = create_agent()
    response_parts = []
    for chunk in agent_executor.stream({"messages": [HumanMessage(content=prompt)]}):
        if "agent" in chunk and "messages" in chunk["agent"]:
            response_parts.extend(
                message.content
                for message in chunk["agent"]["messages"]
                if message.content
            )
    return response_parts[-1] if response_parts else "I could not generate a response."


def main():
    st.set_page_config(
        page_title="Python AI Chatbot",
        page_icon="💬",
        layout="centered",
    )
    st.markdown(
        """
        <style>
            .stApp { background: #f4f7fb; }
            [data-testid="stChatMessage"] { border-radius: 14px; padding: 0.8rem 1rem; }
            [data-testid="stChatMessage"] p { color: #1c2733; }
            h1 { color: #183153; letter-spacing: -0.02em; }
            .subtitle { color: #637083; margin-top: -0.7rem; margin-bottom: 1.5rem; }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.title("Python AI Chatbot")
    st.markdown('<p class="subtitle">Powered by Groq and LangGraph</p>', unsafe_allow_html=True)

    with st.sidebar:
        st.header("Chat controls")
        st.caption("Ask questions, calculate sums, or request a greeting.")
        if st.button("Clear conversation", use_container_width=True):
            st.session_state.messages = []
            st.rerun()
        st.divider()
        st.caption(f"Model: {os.getenv('GROQ_MODEL', 'qwen/qwen3.6-27b')}")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "Hello! I am your Python AI assistant. Ask me anything, or try a calculation.",
            }
        ]

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Message your assistant..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            if not os.getenv("GROQ_API_KEY"):
                response = "GROQ_API_KEY is missing. Add it to your .env file and restart Streamlit."
                st.warning(response)
            else:
                with st.spinner("Thinking..."):
                    try:
                        response = get_response(prompt)
                        st.markdown(response)
                    except Exception as error:
                        response = f"I could not connect to Groq. {error}"
                        st.error(response)
        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()
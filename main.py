import os
import warnings

from langchain_core.messages import HumanMessage
from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

# Suppress warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

# Load environment variables from .env
load_dotenv()


@tool
def calculator(a: float, b: float) -> str:
    """Useful for performing basic arithmetic calculations with numbers."""
    print("Tool has been called.")
    return f"The sum of {a} and {b} is {a + b}"


@tool
def say_hello(name: str) -> str:
    """Useful for greeting a user."""
    print("Tool has been called.")
    return f"Hello {name}, I hope you are well today"


def main():
    groq_key = os.getenv("GROQ_API_KEY")
    model_name = os.getenv("GROQ_MODEL", "qwen/qwen3.6-27b")

    print(f"Initializing Groq model: {model_name}...")

    if not groq_key:
        print("Warning: GROQ_API_KEY is not set in environment.")

    model = ChatGroq(
        model=model_name,
        temperature=0
    )

    tools = [calculator, say_hello]

    agent_executor = create_react_agent(
        model,
        tools
    )

    print("Welcome! I'm your PythonAIChatbot assistant. Type 'quit' to exit.")
    print("You can ask me to perform calculations or chat with me.")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        print("\nAssistant: ", end="")

        for chunk in agent_executor.stream(
            {
                "messages": [
                    HumanMessage(content=user_input)
                ]
            }
        ):
            if "agent" in chunk and "messages" in chunk["agent"]:
                for message in chunk["agent"]["messages"]:
                    print(message.content, end="")

        print()


if __name__ == "__main__":
    main()

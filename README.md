# Groq Chatbot

A lightweight Streamlit chatbot built with Python, LangChain, LangGraph, and Groq. The app lets you chat with a Groq-hosted model and use small custom tools such as a calculator and a greeting helper.

## Overview

This project creates a browser-based ReAct-style agent that:

- accepts chat messages from the user,
- sends them to a Groq model through LangChain,
- decides whether a registered tool should be used,
- and returns the result in a Streamlit chat UI.

It is a simple example of an AI agent that can reason and call tools in a real web app.

## Features

- Streamlit chat interface
- Groq model integration using `langchain-groq`
- ReAct agent created with `langgraph`
- Built-in tools:
  - calculator
  - greeting
- Tool controls available from the `+` popover in the UI
- Environment-based configuration via `.env` or Streamlit secrets
- Message history stored in `st.session_state`

## App Behavior

The current app does the following:

1. Loads environment variables using `python-dotenv`.
2. Retrieves the Groq API key from either `.env` or `st.secrets`.
3. Creates a ReAct agent with the selected Groq model.
4. Registers custom tools for arithmetic and greetings.
5. Displays a chat interface with a `+` button for direct tool use.
6. Sends user prompts to the agent and renders the model response in the chat.

## Project Structure

```text
groq_chatbot_project/
├── main.py
├── requirements.txt
├── README.md
├── .env                  # optional local environment file
├── .streamlit/
│   └── secrets.toml      # optional Streamlit secrets file
└── .venv/                # optional local virtual environment
```

## Tech Stack

- Python
- Streamlit
- LangChain Core
- LangChain Groq
- LangGraph
- python-dotenv

## Prerequisites

Before running the app, make sure you have:

- Python 3.10 or newer
- A Groq API key
- Access to a terminal or PowerShell

## Setup

### 1. Open PowerShell in the project folder

```powershell
cd c:\abhi\groq_chatbot_project
```

### 2. Create and activate a virtual environment

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run this once first:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### 3. Install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Add your Groq credentials

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=qwen/qwen3.6-27b
```

You can also configure the same values in Streamlit secrets if you are deploying through Streamlit Cloud:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
GROQ_MODEL = "qwen/qwen3.6-27b"
```

## Run the App

```powershell
streamlit run main.py
```

Then open the local URL shown in the terminal in your browser.

## Using the App

You can:

- type a normal chat message in the input box,
- use the `+` popover to run the calculator or greeting tools,
- ask questions that may trigger the available tools automatically.

### Example prompts

```text
What is 12 + 8?
Hello Alice
Can you greet my friend Sam?
```

The assistant will use the Groq model and may call the registered tools when needed.

## Tool Details

### Calculator

The calculator tool accepts two numeric inputs and returns the sum.

### Greeting

The greeting tool accepts a name and returns a friendly greeting string.

## Deployment Notes

For Streamlit Community Cloud:

1. Push `main.py`, `requirements.txt`, and `README.md` to GitHub.
2. Do not commit your local `.env` file.
3. Add your Groq secrets in the app settings.
4. Set the main file to `main.py`.

## Notes

- If `GROQ_API_KEY` is missing, the app shows an error and stops before starting the chat.
- The app checks both `.env` values and `st.secrets`, which makes it easy to run locally or deploy in the cloud.
- The tool set is intentionally small and can be expanded by adding more LangChain tools.

## Future Improvements

Possible enhancements include:

- more tools such as weather, search, or file access,
- better error handling and validation,
- conversation logging,
- richer UI elements and more agent capabilities.

# Python AI Chatbot

A lightweight conversational AI assistant built with Python, LangChain, LangGraph, and Groq. The app allows users to chat with an LLM and invoke simple custom tools like a calculator and greeting function.

## Overview

This project creates a ReAct-style agent that:

- accepts text input from the user,
- sends it to a Groq-hosted language model,
- decides whether to use available tools,
- and returns a response in the terminal.

It is ideal for learning how to build a tool-using AI agent with a small, practical example.

## Features

- Command-line chat interface
- Groq model integration via LangChain
- Tool calling with:
  - calculator
  - say_hello
- Environment-based configuration through a `.env` file
- Simple and easy-to-extend architecture

## Architecture

```mermaid
flowchart TD
    A[User Input] --> B[main.py]
    B --> C[Environment Configuration<br/>load_dotenv()]
    B --> D[Tool Definitions<br/>calculator(), say_hello()]
    B --> E[Interactive Loop<br/>while True]

    E --> F[LangChain]
    F --> G[ChatGroq<br/>Groq Model]
    E --> H[LangGraph]
    H --> I[ReAct Agent<br/>create_react_agent()]

    G --> I
    D --> I

    I --> J[Groq LLM API]
    J --> K[Agent Response]
    K --> L[Terminal Output]

    I --> M{Tool Call Needed?}
    M -->|Yes| D
    M -->|No| K
```

This project follows a ReAct-style agent flow:

1. The user enters input in the terminal.
2. `main.py` loads environment variables and initializes the Groq model.
3. The app registers custom tools such as the calculator and greeting tool.
4. LangGraph creates a ReAct agent that can reason and decide whether a tool should be used.
5. The model responds through the Groq API and prints the result back to the terminal.

### Main components

- `main.py`: application entry point
- `requirements.txt`: Python dependencies
- `.env`: holds the Groq API key and model configuration
- `.venv`: local virtual environment used for project dependencies

## Project Structure

```text
project/
├── .env
├── .venv/
├── main.py
├── requirements.txt
└── README.md
```

## Technologies Used

- Python 3
- LangChain Core
- LangChain Groq
- LangGraph
- python-dotenv

## Prerequisites

Before running the project, ensure you have:

- Python 3.10 or newer
- A Groq API key
- Access to the terminal / PowerShell

## Step-by-Step Setup with `.venv`

### 1. Open PowerShell in the project folder

```powershell
cd c:\abhi\preoject
```

### 2. Create a virtual environment

```powershell
py -3 -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, run this once in the current terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Upgrade pip

```powershell
python -m pip install --upgrade pip
```

### 5. Install dependencies

```powershell
pip install -r requirements.txt
```

### 6. Create a `.env` file

Create a file named `.env` in the project root with the following contents:

```env
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=qwen/qwen3.6-27b
```

You can replace the model value with any Groq-supported model you prefer.

### 7. Run the chatbot

```powershell
python main.py
```

## Example Usage

Once the app starts, you can type prompts like:

```text
You: What is 12 + 8?
You: Hello Alice
You: Tell me a joke
```

The assistant will respond using the Groq model and may call the registered tools when needed.

## Exit the Program

Type:

```text
quit
```

to exit the chatbot.

## Notes

- The project loads environment variables from `.env` using `python-dotenv`.
- If `GROQ_API_KEY` is missing, the app prints a warning but will still try to run depending on the environment.
- The current tool set is intentionally simple, making the project a good starting point for more advanced agent workflows.

## Future Enhancements

Possible improvements include:

- adding more tools such as search, file reading, or weather APIs,
- supporting web requests,
- adding a web UI,
- logging conversations,
- improving error handling and model configuration.

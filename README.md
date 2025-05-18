# AI Chatbot with Web Scraping RAG agent

This project is a **two-part machine test** designed to demonstrate AI engineering proficiency in Python, LangChain, OpenAI API integration, REST API development, and session-based chat handling. 

It includes:

- **Task 1**: A web scraper that uses LangChain to extract, embed, and store content from a given URL into a vector store 
- **Task 2**: A RESTful chat API using Fastapi that integrates OpenAI GPT with LangChain, leverages RAG (retrieval-augmented generation), and supports user sessions,    message history, and intelligent agent transfer.


## Installation

- Create a virtual environment: (recommended)

Linux/macOS:

```bash
  # Create a virtual environment
    python3 -m venv .venv

  # Activate the virtual environment
    source .venv/bin/activate
  
```

 Windows:

```powershell
  # Create a virtual environment
    python -m venv .venv

  # Activate the virtual environment
    .venv\Scripts\activate
  
```


- install requirements:
  
```bash
  pip install -r requirements.txt
```


- run task-1(go to task1 directory):


```bash
  cd machine_test/task1
```

- run main.py to execute task-1:


```bash
  python main.py
```


- go to localhost:8000/ and give the url
___________________________________________________________________________________________________________________





- run task-2(go to task2 directory):


```bash
  cd machine_test/task2
```

- run main.py to execute task-2:


```bash
  python main.py
```


- go to localhost:7000/ to intract with chatbot ui and localhost:7000/docs to test in swaggerui


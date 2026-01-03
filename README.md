# Multi-LLM-LangChain_Type

## Overview
**Multi-LLM-LangChain_Type** is a Python project that allows you to interact with multiple Large Language Models (LLMs) simultaneously using [LangChain](https://www.langchain.com/) and [OpenRouter](https://openrouter.ai/).  
The program takes a user prompt and sends it to several models in sequence, returning their responses for comparison.

---

## Features
- Query multiple models (Gemini, LLaMA, DeepSeek, Mistral, GPT‑OSS, etc.).
- Easily switch between models.
- Measure response time for each model.
- Simple terminal interface.
- `.env` support for secure API key storage.

---

## Technologies Used
- **Python 3.9+**
- **LangChain**
- **langchain-openai**
- **langchain-core**
- **dotenv**
- **OpenRouter API**

---

## Project Structure
```
Multi-LLM-LangChain_Type/
│── langchain/
│   ├── main.py        # Main code
│   ├── .env           # API_KEY (do not push to GitHub!)
│   └── .gitignore     # Ignored files
│── README.md          # Documentation
```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/MykhailoTymoshenko08/Multi-LLM-LangChain_Type.git
   cd Multi-LLM-LangChain_Type/langchain
   ```
   
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate # Windows
   ```
   
3. Install dependencies:
   ```bash
   pip install langchain-openai langchain-core python-dotenv
   ```
   
4. Add your API key to .env:
   ```bash
   API_KEY=your_openrouter_api_key
   ```

## Usage
1. Run the project:
   ```bash
   python main.py
   ```
   
2. The program will prompt you to enter a request:
   Enter your request: Hello, what is LangChain?

3. You will then receive responses from all models:
   ```bash
   [1/6] mistralai/devstral-2512:free
   ✅ Model response... (time: 1.23s)
   --------------------------------------------------
   [2/6] google/gemini-2.0-flash-exp:free
   ✅ Model response... (time: 0.98s)
   --------------------------------------------------
   ...
   ```


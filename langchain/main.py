import os
import time

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
API_KEY = os.getenv("API_KEY")


def get_langchain_answer(model_name, user_text):
    start_time = time.time()
    try:
        # 1. Create llm
        llm = ChatOpenAI(
            model = model_name,
            openai_api_key = API_KEY,
            base_url = "https://openrouter.ai/api/v1",
            max_tokens = 200
        ) 

        # 2. Create: prompt, parser, chain
        prompt = ChatPromptTemplate.from_template("{topic}")
        output_parser = StrOutputParser()
        chain = prompt | llm | output_parser

        # 3. Call chain.invoke()
        result = chain.invoke({"topic": user_text})

        elapsed = time.time() - start_time
        return f"✅{result} (час: {elapsed:.2f}с)"
    
    except Exception as e:
        return f"❌Error: {str(e)}"
    
def main():
    models = [''
        "mistralai/devstral-2512:free",
        "google/gemini-2.0-flash-exp:free",
        "google/gemma-3-27b-it:free",
        "openai/gpt-oss-120b:free",
        "deepseek/deepseek-r1-0528:free",
        "meta-llama/llama-3.3-70b-instruct:free",
    ]

    user_prompt = input("Enter your request: ")

    for i, model in enumerate(models, 1):
        print(f"\n[{i}/{len(models)}] {model}")
        answer = get_langchain_answer(model, user_prompt)
        print(answer)
        print("-" * 50)

if __name__ == "__main__":
    main()

def show_menu():
    print("\n" + "="*50)
    print("1. Ask new question")
    print("2. Change model's list")
    print("3. Exit")
    return input("Choose option: ")
import openai

ollama_api_key = "ollama"
ollama_base_url = "http://localhost:11434/v1"

openai_client = openai.OpenAI(base_url=ollama_base_url, api_key=ollama_api_key)

def get_ollama_response(user_query):
    conversation_messages = [
        {"role": "system", "content": "You are a GODLIKE Python Programmer"},
        {"role": "user", "content": user_query}
    ]
    
    ai_response = openai_client.chat.completions.create(
        model="deepseek-coder-v2",
        messages=conversation_messages
    )
    
    return ai_response.choices[0].message.content

helper = ("Write a python code function that can save a file in our CWD:")

print(helper)
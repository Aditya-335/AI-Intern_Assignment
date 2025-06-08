from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()  

client = OpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv("GROQ_API_KEY")  
)

def call_groq(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        content = response.choices[0].message.content
        print("AI raw response:", content)  # <-- Print the actual response content here
        return content
    except Exception as e:
        print(f"Error calling Groq API: {e}")
        raise

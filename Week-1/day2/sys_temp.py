import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq
load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")
if not my_api_key:
    raise ValueError("api key not found")
client = Groq(api_key=my_api_key)
model = "llama-3.3-70b-versatile"
role = "user"
prompt = "suggest name for My Clothing brand?."

#System prompt for the LLM
system_message = {
    "role": "system", 
    "content": "You are a brand manager who suggests name for my company. name should be in one word. suggest only five name"
}
message = {
    "role": role, 
    "content": prompt
    }

messages = [system_message, message]
# Temperature by default is 0 meaning safe. range is [0,2]
response = client.chat.completions.create(model=model, messages=messages, temperature=0)
print(response)

print("#####################################################")
answers = response.choices[0].message.content
print(answers)
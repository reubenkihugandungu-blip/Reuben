# # In VS Code (requires: pip install openai, python-dotenv)
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a direct, no-nonsense fitness coach."},
        {"role": "user",   "content": "James slept 6 hours and hit 7800 steps. What should he do tomorrow?"}
    ]
)

# Extract the text
reply = response.choices[0].message.content
print(reply)

# Use gpt-4o-mini for fast, cheap responses. Use gpt-4o for higher quality on complex tasks.
#  The API call is identical for both; only the model name changes.
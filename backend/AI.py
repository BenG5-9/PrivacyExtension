from extract_policy import extract_policy
from openai import OpenAI
from dotenv import load_dotenv
import os

def run_ai(policy):

  # API key stored in .env for protection
  # Used to retrieve the API key
  # Alternatively api_key = (Personal OpenAI Key) can be used
  load_dotenv()
  client = OpenAI(
      api_key = os.getenv("AI_KEY"),
  )

  response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
      # System-content: Specifications given to the AI bot
      # User-content: Privacy Policy that was pulled from extract_policy.py
      {"role": "system", "content": "Given a string of words, find me what info is being collected, what it might be used for, who might use it"},
      {"role": "user", "content": policy}
    ],
    temperature=1,
    max_tokens=300,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  return response.choices[0].message.content
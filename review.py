import openai
import requests
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_review(diff_url):
    diff = requests.get(diff_url).text
    prompt = f"Review this code diff and provide concise feedback:\n{diff}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

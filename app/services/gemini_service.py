import os
import requests
from dotenv import load_dotenv

load_dotenv()

def ask_gemini(prompt: str):
    api_key = os.getenv("GEMINI_API_KEY", "").strip()

    

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={api_key}"

    headers = {
        "Content-Type": "application/json"
    }

    body = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(
        url,
        headers=headers,
        json=body,
        timeout=60
    )


    response.raise_for_status()

    return response.json()["candidates"][0]["content"]["parts"][0]["text"]
import requests
from config import key

def chat(chat_query):
    url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-pro:generateContent?key={key}"

    headers = {
        "Content-Type": "application/json"
    }

    data = {
        "contents": [
            {
                "role": "user",
                "parts": [
                    {"text": chat_query}
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        try:
            # print("result for the api request:\n ",result)
            # Extract the content from the response
            content = result["candidates"][0]["content"]["parts"][0]["text"]
            return content
        except (KeyError, IndexError):
            print("Unexpected response format:", result)
    else:
        print(f"Request failed with status {response.status_code}: {response.text}")

# chat("Who is MS Dhoni?")
# chat("Write a program to find the factorial of a number.")


def get_gemini_models():
    """Get the list of available Gemini models."""
    url = f"https://generativelanguage.googleapis.com/v1/models?key={key}"
    response = requests.get(url)
    print(response.status_code)
    print(response.text)
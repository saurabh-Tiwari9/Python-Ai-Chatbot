
import os
from openai import OpenAI

# Connect to Google's Gemini API
client = OpenAI(
    api_key=os.environ["GEMINI_API_KEY"],
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

print("Gemini chatbot started! Type 'exit' to stop.")

while True:
    user_input = input("\nYou: ").strip()

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    if not user_input:
        continue

    try:
        response = client.chat.completions.create(
            model="gemini-3.8-flash",
            messages=[
                {
                    "role": "system",
                    "content": "You are a friendly AI assistant."
                },
                {
                    "role": "user",
                    "content": user_input
                }
            ],
            temperature=0.7,
            max_tokens=150
        )

        print("\nBot:", response.choices[0].message.content)

    except Exception as error:
        print("\nAPI error:", error)

from openai import OpenAI
from config import OPENAI_API_KEY, SYSTEM_PROMPT

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_reply(player: str, mebius_nickname: str, message: str) -> str:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or gpt-4
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT.replace("{mebius_nickname}", mebius_nickname)},
            {"role": "user", "content": f"{player}: {message}\nMEBIUSとして返答せよ。"}
        ],
        temperature=0.8,
        max_tokens=150
    )
    return response.choices[0].message.content.strip() if response.choices[0].message.content else ""
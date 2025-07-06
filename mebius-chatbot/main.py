# main.py

from fastapi import FastAPI, Request
from pydantic import BaseModel
from llm.generator import generate_reply

app = FastAPI()

class ChatInput(BaseModel):
    player: str
    message: str

@app.post("/chat")
async def chat_endpoint(input_data: ChatInput):
    reply = generate_reply(input_data.player, input_data.message)
    return {"reply": reply}
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from llm.generator import generate_reply  # あなたの応答ロジック

app = FastAPI()

# テンプレートと静的ファイルのパスを設定
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request, "response": None})


@app.post("/", response_class=HTMLResponse)
async def chat(request: Request, player: str = Form(...), mebius_nickname: str = Form(...), message: str = Form(...)):
    reply = generate_reply(player, mebius_nickname, message)

    print(f"Received message from {player}: {message}")
    print(f"Mebius ({mebius_nickname}) replied: {reply}")

    return templates.TemplateResponse("chat.html", {
        "request": request, 
        "response": reply, 
        "player": player, 
        "mebius_nickname": mebius_nickname,
        "message": message})
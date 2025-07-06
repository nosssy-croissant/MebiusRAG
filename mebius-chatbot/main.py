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
async def chat(request: Request, player: str = Form(...), message: str = Form(...)):
    reply = generate_reply(player, message)
    return templates.TemplateResponse("chat.html", {"request": request, "response": reply, "player": player, "message": message})
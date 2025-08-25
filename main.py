# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mini App</title>
        <script src="https://telegram.org/js/telegram-web-app.js"></script>
    </head>
    <body>
        <h1>Привет из Mini App!</h1>
        <button onclick="sendData()">Отправить данные боту</button>

        <script>
            let tg = window.Telegram.WebApp;
            tg.expand();

            function sendData() {
                tg.sendData(JSON.stringify({msg: "Hello from Mini App"}));
            }
        </script>
    </body>
    </html>
    """

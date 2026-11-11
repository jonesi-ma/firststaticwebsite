from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

app = FastAPI()
app.mount("/files", StaticFiles(directory="HTML"), name="files")

@app.get("/")
def website_home():
    with open("HTML/Practice_HTML.html", "r", encoding="utf-8") as f:
        html_content = f.read()
    return HTMLResponse(content=html_content, status_code=200)
from typing import Union

from fastapi import FastAPI, Request, Form
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import tkinter as tk
from tkinter import filedialog as fd
# from starlette.responses import FileResponse 

app = FastAPI()
file_path = ''

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"))

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse('index.html', {"request": request})


@app.post("/button-clicked")
async def handle_button_click(request: Request, action: str = Form(...)):
    global file_path
    if action == "transferbuttonclicked":
        file_path = fd.askopenfilename()
        return templates.TemplateResponse("/index.html", {"request": request, "message": "opened filedialog"})
    return HTMLResponse("<h1>Unknown action</h1>")


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
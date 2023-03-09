from typing import Union

from fastapi import FastAPI

from utils.utils import *

app = FastAPI()


@app.get("/getStyles")
def get_styles():
    return getStyles()


@app.get("/generateImage/{prompt}/{style_id}")
def generate_image(prompt: str, style_id: int):
    return generateImage(prompt=prompt, style_id=style_id)

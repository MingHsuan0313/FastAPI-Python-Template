"""
This is my own custom module for
demonstration purposes.

Functions:
    root()
"""
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"message": "Hello World"}

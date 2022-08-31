"""
This is my own custom module for
demonstration purposes.

Functions:
    root()
"""
from fastapi import FastAPI
from pydantic import BaseModel


class Test(BaseModel):
    """_summary_

    Args:
        BaseModel (_type_): _description_
    """

    name: str


app = FastAPI()


@app.get("/")
async def root():
    """_summary_

    Returns:
        _type_: _description_
    """
    return {"message": "Hello World"}

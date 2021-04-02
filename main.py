import os
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    FLAG = os.environ["FLAG"]
    return {"message": "Take my flag", "flag": FLAG}

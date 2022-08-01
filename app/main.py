import os
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

from . import kfs_router

app = FastAPI()

app.include_router(kfs_router.router)


@app.get("/")
def root():
    a = "a"
    b = "b" + a
    return {"hello world": b}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=os.environ.get("PORT", 8080))

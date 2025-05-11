from fastapi import FastAPI
from typing import Optional  # Required for Python < 3.10

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):  # or q: str | None = None in Python 3.10+
    return {"item_id": item_id, "q": q}

# main.py
from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
from chat_agent import get_current_time  # Updated import

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/chat/")
async def chat(message: Message):
    response = await get_current_time()
    return {"response": response.final_output}
    
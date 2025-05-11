# 🚀 FastAPI Simple API

This is a minimal FastAPI project with two endpoints to get started quickly.

## 🧰 Requirements

- Python 3.7+
- FastAPI
- Uvicorn

## ⚙️ Setup

1. Install dependencies:
   
   pip install fastapi uvicorn
Run the app:


uvicorn main:app --reload
🌐 API Endpoints
GET /
Returns: {"Hello": "World"}

GET /items/{item_id}?q=your_query
Returns item with optional query.

📘 Example

GET /items/5?q=test
Response: {"item_id": 5, "q": "test"}
🧾 Notes
Interactive docs: http://127.0.0.1:8000/docs

Optional query param handled with Optional[str] from typing.




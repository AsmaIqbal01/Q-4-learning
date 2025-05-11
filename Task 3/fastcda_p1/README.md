
# DACA Chatbot API

A FastAPI-based API for interacting with a chatbot in the DACA series.

## Features

- Retrieve user information by user ID.
- Send messages to the chatbot and receive responses.
- Automatically generates metadata for each message.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/daca-chatbot-api.git
   cd daca-chatbot-api
Install dependencies:


pip install fastapi uvicorn pydantic
Run the application:


uvicorn main:app --reload
API Endpoints
GET /: Welcome message.
GET /users/{user_id}: Retrieve user information.
POST /chat/: Send a message to the chatbot and receive a reply.
Models
Metadata: Contains timestamp and session_id.
Message: Includes user_id, text, metadata, and optional tags.
Response: Contains user_id, reply, and metadata.
License
This project is licensed under the MIT License.


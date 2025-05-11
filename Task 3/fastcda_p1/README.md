
# DACA Chatbot API

A FastAPI-based API for interacting with a chatbot in the DACA series.

## Features

- Retrieve user information by user ID.
- Send messages to the chatbot and receive responses.
- Automatically generates metadata for each message.

user information.
POST /chat/: Send a message to the chatbot and receive a reply.
Models
Metadata: Contains timestamp and session_id.
Message: Includes user_id, text, metadata, and optional tags.
Response: Contains user_id, reply, and metadata.
License
This project is licensed under the MIT License.


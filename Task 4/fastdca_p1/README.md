# FastAPI Parameter Types Guide

This document provides a comprehensive overview of parameter handling in FastAPI, covering various parameter types, validation, metadata, and automatic API documentation features.

## Parameter Types in FastAPI

FastAPI supports multiple parameter types to handle incoming request data efficiently and flexibly:

### 1. Path Parameters
- Defined as parts of the URL path.
- Used to capture variable segments in the URL.
- Example:
  ```python
  @app.get("/items/{item_id}")
  async def read_item(item_id: int):
      return {"item_id": item_id}
2. Query Parameters
Sent as key-value pairs after ? in the URL.
Can be optional or required and support validation.
Use Query for extra validation and metadata.
Example:
python
3 lines
Click to expand
@app.get("/items/")
async def read_items(q: str | None = Query(None, min_length=3, max_length=50)):
...
3. Request Body Parameters
Contain JSON or other structured data sent in the body of the request.
Defined using Pydantic models for validation and serialization.
Example:
python
8 lines
Click to expand
class Item(BaseModel):
name: str
...
4. Header Parameters
Extracted from HTTP request headers.
Defined using the Header dependency.
Example:
python
5 lines
Click to expand
from fastapi import Header
...
5. Cookie Parameters
Extracted from HTTP cookies sent with the request.
Defined using the Cookie dependency.
Example:
python
5 lines
Click to expand
from fastapi import Cookie
...
Validation and Metadata
FastAPI allows adding validation rules and metadata to parameters for improved data integrity and documentation:

Validation examples: minimum/maximum values, string length, regex patterns.
Metadata: titles, descriptions, and examples for API docs.
Example with validation and metadata:
python
15 lines
Click to expand
from fastapi import FastAPI, Query
...
Automatic API Documentation
FastAPI automatically generates interactive API docs using OpenAPI standards:

Swagger UI: Accessible at /docs for interactive API testing.
ReDoc: Accessible at /redoc for structured API documentation.
Enhancing Documentation
You can enhance docs by:

Adding descriptions and examples to parameters.
Using Enums to restrict values.
Grouping related parameters for clarity.
Summary
Understanding and effectively using FastAPI’s parameter types and validation features enables you to build robust, well-documented APIs effortlessly.


# 📝 FastAPI To-Do List

This is a simple FastAPI project that allows you to manage a basic to-do list. You can add items, list them, update, delete, and retrieve individual items by their ID.

## 🚀 Features

- **Add** new to-do items (POST `/items`)
- **List** all to-do items with optional limit (GET `/items`)
- **Get** a specific item by ID (GET `/items/{item_id}`)
- **Update** an existing item (PUT `/items/{item_id}`)
- **Delete** an item by ID (DELETE `/items/{item_id}`)
- Simple in-memory storage (no database)

## 📦 Requirements

- Python 3.10+
- FastAPI
- Uvicorn
- Pydantic

Install the dependencies with:

```bash
pip install fastapi uvicorn
```

## ▶️ How to Run

```bash
uvicorn main:app --reload
```

Then open your browser and go to:

- App: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
- API Docs (Swagger UI): [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📌 Example Item JSON

```json
{
  "text": "Buy groceries",
  "is_done": false
}
```

## 📁 Endpoints Overview

| Method | Path                | Description                  |
|--------|---------------------|------------------------------|
| GET    | `/`                 | Hello World root route       |
| POST   | `/items`            | Add a new to-do item         |
| GET    | `/items`            | List all to-do items         |
| GET    | `/items/{item_id}`  | Get a specific item          |
| PUT    | `/items/{item_id}`  | Update an existing item      |
| DELETE | `/items/{item_id}`  | Delete a specific item       |

## 📎 Notes

- This app uses a simple Python list for storing items.
- **All data is lost when the server restarts.**
- For production use, consider integrating a **database** and adding **persistent storage**.

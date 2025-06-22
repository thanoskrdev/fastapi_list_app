# 🐍 Simple FastAPI To-Do App

This is a simple FastAPI project that allows you to manage a basic to-do list. You can add items, list them, and retrieve individual items by their index.

## 🚀 Features

- Add new to-do items (`POST /items`)
- List all to-do items with optional limit (`GET /items`)
- Get a specific item by ID (`GET /items/{item_id}`)
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

- Open your browser and go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- To explore the API docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📌 Example Item JSON

```json
{
  "text": "Buy groceries",
  "is_done": false
}
```

## 📁 Endpoints Overview

| Method | Path              | Description             |
|--------|-------------------|-------------------------|
| GET    | `/`               | Hello World root route  |
| POST   | `/items`          | Add a new to-do item    |
| GET    | `/items`          | List all to-do items    |
| GET    | `/items/{item_id}`| Get a specific item     |

## 📎 Notes

- This app uses a simple Python list for storing items. All data is lost when the server restarts.
- For production, consider adding a database and proper data persistence.

---



# 🧠 Document Q&A Microservice System

This system simulates a backend architecture for an **AI document Q&A platform**, using Python microservices with FastAPI, PostgreSQL, and async background tasks.

---

## 🚀 Services

| Service          | Description                    | URL                     |
|------------------|--------------------------------|-------------------------|
| Document Service | Store & retrieve documents     | http://localhost:8001    |
| Question Service | Submit & check questions       | http://localhost:8002    |

---

## 🧰 Tech Stack

- FastAPI + SQLAlchemy Async  
- PostgreSQL (1 per microservice)  
- Docker & Docker Compose  
- Async background processing  
- HTTP inter-service communication  

---

## 📦 Setup Instructions

1. **Clone the repo**

2. **Run services** (API Gateway removed, services accessed directly)
   ```bash
   docker-compose up --build
````

3. Visit services directly:

   * Document Service: [http://localhost:8001/health](http://localhost:8001/health)
   * Question Service: [http://localhost:8002/health](http://localhost:8002/health)

---

## 🔗 API Usage

### Upload Document

```http
POST /documents/
Content-Type: application/json

{
  "title": "My Doc",
  "content": "This is the content"
}
```

### Get Document

```http
GET /documents/{id}
```

### Ask a Question

```http
POST /questions/
Content-Type: application/json

{
  "document_id": 1,
  "question": "What is this about?"
}
```

### Check Question Status

```http
GET /questions/{id}
```

---

## ✅ Health Checks

* `/health` endpoint available on every service.

---

## 📌 Notes

* Questions are answered asynchronously with a delay (\~5 seconds).
* Each microservice is independently accessible — no API Gateway in use.
* Each service manages its own database.
* Microservices communicate via HTTP requests directly.

---

## 🏗️ Architecture

* This is a **microservice architecture**:
  Independent services running separately with dedicated databases and APIs.

---




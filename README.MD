-----------------------------------------------------------------
# 🚀 Dear AI — SSIP Project

![status](https://img.shields.io/badge/status-active-brightgreen) ![license](https://img.shields.io/badge/license-MIT-blue)

Dear AI is an empathetic conversational backend built to provide supportive, non-clinical mental health companionship using large language models. This repository contains the API, persistence layer, and AI orchestration components for context-aware chat sessions.

Table of Contents
-----------------
- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Quick Start](#quick-start)
- [Configuration & Environment](#configuration--environment)
- [Database Schema](#database-schema)
- [Running the Backend](#running-the-backend)
- [API Endpoints (examples)](#api-endpoints-examples)
- [Folder Structure](#folder-structure)
- [Contributing](#contributing)
- [Security & Privacy](#security--privacy)
- [License](#license)

## Project Overview

Purpose: Provide a backend for an AI companion focused on attentive listening, emotional validation, and gentle coping suggestions. It is intended for supportive conversations and explicitly not a replacement for professional mental health care.

Target users: developers building front-ends (web, mobile, or chat UI) that need a context-aware AI assistant, and researchers exploring compassionate dialogue agents.

Goals:

- Deliver concise, context-aware AI responses.
- Persist conversation history to enable session continuity.
- Keep the architecture modular so model providers and pipelines can be swapped.

This project uses LangChain adapters to integrate model providers (Google Generative AI, HuggingFace, etc.) and PostgreSQL for storing chat data.

## Features

- Empathetic, context-aware chat responses.
- Persistent chat histories stored in PostgreSQL.
- Modular AI layer (LangChain client + provider adapters).
- Clear request/response validation using Pydantic schemas.
- Environment-driven configuration (via `.env`).

## Tech Stack

- Python 3.x
- FastAPI — API server
- LangChain — orchestration / prompt handling
- Google Generative API, HuggingFace (via LangChain) — LLM providers
- PostgreSQL — persistent storage
- psycopg2-binary — DB adapter
- Uvicorn / Gunicorn — ASGI server for dev/prod

## Quick Start

1. Clone the repo and enter the directory:

```powershell
git clone <repo-url>
cd "Dear AI"
```

2. Create and activate a virtual environment (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Install dependencies:

```powershell
pip install -r requirements.txt
```

4. Create a `.env` file at project root (see next section).

## Configuration & Environment

Copy a `.env.example` to `.env` (or create `.env`) and set values for secrets and DB credentials. Minimum recommended entries:

```
USER=<db_user>
PASSWORD=<db_password>
HOST=<db_host>
PORT=<db_port>
DBNAME=<database_name>
GOOGLE_API_KEY=<google_api_key>
HUGGINGFACE_API_KEY=<huggingface_api_key>
OPENAI_API_KEY=<openai_api_key>
```

Important: Never commit secrets to the repository. Use environment variables or a secrets manager for production.

## Database Schema

Suggested minimal schema to get started (PostgreSQL):

```sql
CREATE TABLE user_info (
	user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	username TEXT NOT NULL,
	created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE chats (
	chat_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
	chat_name TEXT NOT NULL,
	user_id UUID REFERENCES user_info(user_id),
	created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE conversations (
	id SERIAL PRIMARY KEY,
	chat_id UUID REFERENCES chats(chat_id),
	role TEXT,
	message TEXT,
	created_at TIMESTAMP DEFAULT NOW()
);
```

Place SQL scripts under a `db/` directory, or add Alembic for proper migration management.

## Running the Backend

Start a development server with auto-reload:

```powershell
uvicorn api:app --reload
```

For production use, run with Gunicorn + Uvicorn workers:

```powershell
gunicorn -k uvicorn.workers.UvicornWorker api:app
```

## API Endpoints (examples)

The code defines API routes in `api.py` using Pydantic validators from `Schemas/`. Example endpoints (confirm exact paths in `api.py`):

- POST /users — create a user (payload validated by `Schemas/Create_User_validator.py`)
- POST /chats — create a chat session (`Schemas/Create_Chat_validator.py`)
- POST /chat/{chat_id}/message — send a message to the AI and receive a reply
- GET /chat/{chat_id} — retrieve chat metadata or history

Example request (send user message):

```bash
curl -X POST "http://localhost:8000/chat/<chat_id>/message" \
	-H "Content-Type: application/json" \
	-d '{"User_Input": "I'm feeling stressed today."}'
```

Example JSON response (illustrative):

```json
{
	"chat_id": "...",
	"reply": "I hear you — that sounds tough. Tell me more about what's been going on.",
	"timestamp": "2025-11-11T12:00:00Z"
}
```

## Folder Structure

- `api.py` — FastAPI application and route wiring
- `core/` — DB operations (create/update/delete chats and users)
- `Schemas/` — Pydantic models and validators
- `Chat_Repositories/` — DB query helpers (read-only retrievals, checks)
- `AI_Pipeline/` — LangChain client, model orchestration, and history management
- `utils/` — misc helpers (session management)
- `Testing LLM's/` — streamlit demos and local experiment scripts

## Contributing

We welcome contributions. Suggested workflow:

1. Open an issue to propose larger changes.
2. Create a feature branch named `feature/your-change` or `fix/bug`.
3. Open a pull request with a clear description and link to the issue.

Coding standards:

- Follow PEP8. Use `black` for formatting and `flake8` for linting.
- Write tests for new behavior and run them locally before opening PRs.

Helpful commands:

```powershell
pip install black flake8
black .
flake8
```

## Security & Privacy

This project handles sensitive conversational data. For production:

- Use TLS (HTTPS) for all traffic.
- Restrict DB access and enable encryption at rest if available.
- Avoid logging full user messages in plaintext unless necessary and consented to.
- Rotate and protect API keys (use secret managers where possible).

## License

This project is released under the MIT License. Add a `LICENSE` file to the repository if you haven't yet.

## Contact & Acknowledgements

If you need help or want to collaborate, open an issue or contact the maintainers listed in the repo.

Thanks to LangChain and the open-source community for the building blocks used in this project.

-----------------------------------------------------------------

If you'd like further polish, I can:

- Add a `README` screenshot or architecture diagram image.
- Generate API docs automatically (OpenAPI) and include a sample Postman collection.
- Pin dependency versions and validate installation in a virtual environment.

Once you're happy with this version I will mark the README polish task as completed.


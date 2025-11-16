<div align="center">

# 🚀 Dear AI — SSIP Project

**An Empathetic AI Companion for Mental Health Support**

![status](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge)
![version](https://img.shields.io/badge/version-0.0.5-blue?style=for-the-badge)
![license](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![python](https://img.shields.io/badge/python-3.8%2B-brightblue?style=for-the-badge)

[Overview](#-overview) • [Features](#-features) • [Quick Start](#-quick-start) • [API Docs](#-api-documentation) • [Contributing](#-contributing)

</div>

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Version History](#-version-history)
- [Quick Start](#-quick-start)
- [Configuration](#-configuration--environment)
- [Database Schema](#-database-schema)
- [Running the Backend](#-running-the-backend)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Contributing](#-contributing)
- [Security & Privacy](#-security--privacy)
- [License](#-license)

---

## 🎯 Overview

**Dear AI** is a production-ready backend service for an AI-powered mental health companion. It provides empathetic conversational support through multiple interfaces (text, voice) with persistent chat histories, powered by advanced language models and built on modern Python web technologies.

**Purpose:** Enable supportive, non-clinical conversations with context-aware AI responses that listen, validate, and gently guide users.

**Target Users:** 
- Frontend developers building chat interfaces (web, mobile, desktop)
- Researchers exploring compassionate dialogue systems
- Mental health support platforms seeking AI integration

**Core Goals:**
- Deliver empathetic, context-aware responses within milliseconds
- Maintain conversation continuity through persistent storage
- Support multiple interaction modalities (text & voice/audio)
- Provide a modular, extensible architecture for model swapping

> **⚠️ Disclaimer:** This tool is designed for supportive conversation and is not a substitute for professional mental health services. Users in crisis should seek immediate professional help.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| **Context-Aware Responses** | Maintains conversation history for coherent, empathetic replies |
| **Multi-Modal Support** | Text chat and voice/audio interaction via Gemini TTS |
| **Stream Responses** | Real-time response streaming for improved UX |
| **Persistent Storage** | All conversations stored in PostgreSQL for session continuity |
| **Modular AI Layer** | LangChain-based orchestration supporting multiple LLM providers |
| **Request Validation** | Pydantic schemas ensure data integrity |
| **Secure Config** | Environment-based secrets management with `python-dotenv` |
| **Production-Ready** | CORS enabled, error handling, background task support |

---

## 🛠 Tech Stack

```
Backend Framework    FastAPI (async, modern Python web framework)
LLM Orchestration    LangChain (prompt management, provider abstraction)
LLM Providers        Google Generative AI (Gemini 2.5 Pro)
Audio Synthesis      Gemini TTS (text-to-speech)
Database             PostgreSQL (chat persistence)
Database Driver      psycopg2-binary
Data Validation      Pydantic (v2 compatible)
Server               Uvicorn (dev) / Gunicorn (prod)
Environment          python-dotenv
```

---

## 📦 Version History

| Version | Status | Features | Details |
|---------|--------|----------|---------|
| **0.0.1** | ✅ Released | Core endpoints | User creation, chat creation, chat deletion, retrieval (excluding `/chat/audio` & `/chat/text`) |
| **0.0.2** | ✅ Released | Text chat | `/Chat/Text` endpoint for text-based conversational AI |
| **0.0.3** | ✅ Released | Streaming | Streamed text responses for real-time UX |
| **0.0.4** | ✅ Released | Audio Chat | `/Chat/Voice` endpoint with Gemini TTS audio synthesis |
| **0.0.5** | 🔄 Current | Streamed Audio | Voice input → AI response → streamed audio output (production ready) |

**Current Version:** `0.0.5` - Full audio streaming with voice interaction

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- PostgreSQL 12+
- Git

### Setup (PowerShell on Windows)

1. **Clone & Navigate**
   ```powershell
   git clone https://github.com/Dhanam-patel/Dear-AI.git
   cd "Dear AI"
   ```

2. **Create Virtual Environment**
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Configure Environment**
   ```powershell
   # Create .env file with required variables (see Configuration section)
   cp .env.example .env  # if available, or create manually
   ```

5. **Initialize Database**
   ```powershell
   # Run SQL schema (see Database Schema section)
   psql -U <user> -d <database> -f db/init_schema.sql
   ```

6. **Start the Server**
   ```powershell
   uvicorn api:app --reload
   ```

   Server will be available at `http://localhost:8000`

---

## ⚙️ Configuration & Environment

Create a `.env` file in the project root with the following variables:

```bash
# Database Configuration
USER=postgres
PASSWORD=your_db_password
HOST=localhost
PORT=5432
DBNAME=dear_ai_db

# API Keys (choose providers you plan to use)
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACE_API_KEY=your_huggingface_key
OPENAI_API_KEY=your_openai_key

# Server Configuration
API_HOST=0.0.0.0
API_PORT=8000
```

### Environment Notes
- **Never commit `.env` to version control.** Use `.gitignore` to exclude it.
- For production, use a secrets manager (AWS Secrets Manager, HashiCorp Vault, etc.)
- The app uses `python-dotenv` to automatically load variables at startup.

---

## 🗄️ Database Schema

PostgreSQL table definitions (place in `db/init_schema.sql`):

```sql
-- Users Table
CREATE TABLE IF NOT EXISTS user_info (
    user_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INT,
    gender VARCHAR(10),
    city TEXT,
    username TEXT UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Chats Table
CREATE TABLE IF NOT EXISTS chats (
    chat_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    chat_name TEXT NOT NULL,
    user_id UUID NOT NULL REFERENCES user_info(user_id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

-- Conversations Table
CREATE TABLE IF NOT EXISTS conversations (
    id SERIAL PRIMARY KEY,
    chat_id UUID NOT NULL REFERENCES chats(chat_id) ON DELETE CASCADE,
    role VARCHAR(20), -- 'user' or 'assistant'
    message TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Indexes for performance
CREATE INDEX IF NOT EXISTS idx_chats_user_id ON chats(user_id);
CREATE INDEX IF NOT EXISTS idx_conversations_chat_id ON conversations(chat_id);
CREATE INDEX IF NOT EXISTS idx_conversations_created_at ON conversations(created_at);
```

Run this script:
```powershell
psql -U postgres -d dear_ai_db -f db/init_schema.sql
```

---

## 🏃 Running the Backend

### Development Mode
```powershell
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

### Production Mode (with Gunicorn)
```powershell
pip install gunicorn
gunicorn -k uvicorn.workers.UvicornWorker api:app --bind 0.0.0.0:8000 --workers 4
```

### Health Check
```bash
curl http://localhost:8000/health
# Response:
# {
#   "Status": "OK",
#   "Model": "Gemini 2.5 Pro",
#   "Version": "0.0.5"
# }
```

---

## 📡 API Documentation

### Base URL
```
http://localhost:8000
```

### Endpoints Summary

| Method | Endpoint | Description | Status |
|--------|----------|-------------|--------|
| GET | `/` | Welcome message | ✅ v0.0.1 |
| GET | `/health` | Health check & version | ✅ v0.0.1 |
| POST | `/Create/User` | Create a new user | ✅ v0.0.1 |
| POST | `/Create/Chat` | Create a chat session | ✅ v0.0.1 |
| POST | `/Chat/Text` | Send text message → get streaming text response | ✅ v0.0.2 |
| POST | `/Chat/Voice` | Send text → get streaming audio response | ✅ v0.0.4 |
| GET | `/retrieve_chats/{chat_id}` | Get chat history | ✅ v0.0.1 |
| DELETE | `/chat_delete/{chat_id}` | Delete a chat session | ✅ v0.0.1 |

---

### Detailed Endpoint Reference

#### 1. **Create User** `POST /Create/User`

Creates a new user account.

**Request Body:**
```json
{
  "FirstName": "John",
  "LastName": "Doe",
  "Age": 28,
  "Gender": "male",
  "City": "San Francisco",
  "Username": "johndoe_2025"
}
```

**Response (201):**
```json
{
  "message": "User created successfully"
}
```

**Validation Rules:**
- `FirstName`, `LastName`, `City` → title-cased automatically
- `Gender` → lowercase ('male' or 'female')
- `Username` → must be unique

---

#### 2. **Create Chat** `POST /Create/Chat`

Initializes a new chat session for a user.

**Request Body:**
```json
{
  "Chat_Name": "Stress Management Session",
  "User_id": "550e8400-e29b-41d4-a716-446655440000"
}
```

**Response (201):**
```json
{
  "message": "Chat created successfully"
}
```

**Validation Rules:**
- `Chat_Name` → must be unique
- `User_id` → must reference an existing user

---

#### 3. **Send Text Message** `POST /Chat/Text`

Send a text message and receive a streamed text response.

**Request Body:**
```json
{
  "Chat_id": "550e8400-e29b-41d4-a716-446655440001",
  "User_Input": "I've been feeling overwhelmed at work lately."
}
```

**Response (200) — Server-Sent Events (SSE):**
```
data: I hear you—work stress can be really overwhelming...
data: Let's talk about what's been the most challenging...
data: [continues streaming...]
```

**Features:**
- Real-time streaming response via Server-Sent Events
- Automatic conversation history update
- Background task handling

---

#### 4. **Voice Chat** `POST /Chat/Voice`

Send text input → receive AI response as streamed audio (WAV format).

**Request Body:**
```json
{
  "Chat_id": "550e8400-e29b-41d4-a716-446655440001",
  "User_Input": "I'm having a difficult day."
}
```

**Response (200):**
```
Binary audio/wav stream (via Server-Sent Events)
```

**Features:**
- Text input processed by AI
- Response synthesized to speech via Gemini TTS
- Streamed as WAV audio for immediate playback

---

#### 5. **Retrieve Chat History** `GET /retrieve_chats/{chat_id}`

Fetch complete conversation history for a chat session.

**Response (200):**
```json
{
  "chat_id": "550e8400-e29b-41d4-a716-446655440001",
  "messages": [
    {
      "role": "user",
      "message": "I'm feeling stressed.",
      "created_at": "2025-11-11T10:00:00Z"
    },
    {
      "role": "assistant",
      "message": "I hear you. Let's talk about it...",
      "created_at": "2025-11-11T10:00:05Z"
    }
  ]
}
```

---

#### 6. **Delete Chat** `DELETE /chat_delete/{chat_id}`

Permanently remove a chat session and its history.

**Response (200):**
```json
{
  "message": "Chat Session Deleted Successfully"
}
```

---

### Example cURL Requests

**Create a user:**
```bash
curl -X POST "http://localhost:8000/Create/User" \
  -H "Content-Type: application/json" \
  -d '{
    "FirstName": "Jane",
    "LastName": "Smith",
    "Age": 32,
    "Gender": "female",
    "City": "Austin",
    "Username": "janesmith_25"
  }'
```

**Send a text message:**
```bash
curl -X POST "http://localhost:8000/Chat/Text" \
  -H "Content-Type: application/json" \
  -d '{
    "Chat_id": "550e8400-e29b-41d4-a716-446655440001",
    "User_Input": "I need help managing anxiety."
  }'
```

**Retrieve chat history:**
```bash
curl "http://localhost:8000/retrieve_chats/550e8400-e29b-41d4-a716-446655440001"
```

---

## 📁 Project Structure

```
Dear AI/
├── api.py                        # FastAPI app & route definitions
├── requirements.txt              # Python dependencies
├── .env                          # Environment variables (secrets)
├── .env.example                  # Template for .env
│
├── core/                         # Database operations
│   ├── Create_Users_db.py        # User creation logic
│   ├── Create_Chat_db.py         # Chat session creation
│   ├── Delete_Chat_db.py         # Chat deletion
│   └── Update_Conversations.py   # Conversation persistence
│
├── Schemas/                      # Pydantic validators
│   ├── Create_User_validator.py  # User input validation
│   ├── Create_Chat_validator.py  # Chat creation validation
│   ├── Chat_validator.py         # Chat message validation
│   └── Delete_Chat_Validator.py  # Deletion validation
│
├── Chat_Repositories/            # Database query helpers
│   ├── Chat_check.py             # Verify chat existence
│   ├── User_check.py             # Verify user existence
│   ├── Chat_Context.py           # Retrieve conversation history
│
├── AI_Pipeline/                  # LLM orchestration
│   ├── client.py                 # LangChain chat client
│   ├── model.py                  # Model initialization (Gemini)
│   ├── History_manager.py        # Chat history formatting
│   ├── audio_streaming.py        # Audio stream handler
│   └── Audio_Synthesizer.py      # TTS synthesis (Gemini)
│
├── utils/                        # Utility helpers
│   ├── Session_History.py        # Session management
│   ├── Streamed_data_handler.py  # Response streaming logic
│   └── pmc_to_wav_AudioFile.py   # PCM → WAV conversion
│
├── db/                           # Database scripts
│   └── init_schema.sql           # PostgreSQL schema
│
└── Testing LLM's/                # Development & demos
    ├── app.py                    # Streamlit demo UI
    └── Dear_AI.py                # Local testing script
```

---

## 🤝 Contributing

We welcome contributions! Here's how to get involved:

### Contribution Workflow

1. **Fork** the repository
2. **Create a branch:** `git checkout -b feature/your-feature-name`
3. **Make changes** and test locally
4. **Commit:** `git commit -m "feat: add your feature description"`
5. **Push:** `git push origin feature/your-feature-name`
6. **Open a Pull Request** with detailed description

### Code Standards

- **PEP8 Compliance:** All Python code must follow PEP8
- **Formatting:** Use `black` for code formatting
- **Linting:** Run `flake8` before submitting PRs
- **Tests:** Write unit tests for new features

### Development Commands

```powershell
# Format code
pip install black
black .

# Lint code
pip install flake8
flake8 .

# Run tests (if available)
pytest tests/
```

### Issues & Discussions

- **Bug Reports:** Open an issue with reproduction steps
- **Feature Requests:** Describe the use case and expected behavior
- **Questions:** Start a discussion in the GitHub Discussions tab

---

## 🔒 Security & Privacy

This project handles sensitive conversational data. Follow these best practices:

### Security Checklist

- ✅ **Enable HTTPS/TLS** in production (use reverse proxy like Nginx)
- ✅ **Secure Database:** Use strong credentials, restrict network access
- ✅ **Secrets Management:** Never hardcode API keys; use environment variables or secret managers
- ✅ **API Rate Limiting:** Implement rate limiting to prevent abuse
- ✅ **Input Validation:** All inputs validated via Pydantic (built-in)
- ✅ **Logging:** Avoid logging sensitive user messages
- ✅ **Data Retention:** Define and implement data retention policies
- ✅ **Backup Strategy:** Regular database backups with encryption

### Privacy Notes

- Users should be informed that conversations are stored
- Implement GDPR-compliant data deletion mechanisms
- Never share user data with third parties without explicit consent

---

## 📄 License

This project is released under the **MIT License**. See the [LICENSE](LICENSE) file for full details.

---

## 📞 Contact & Support

- **Maintainer:** Dhanam Patel
- **Repository:** [GitHub](https://github.com/Dhanam-patel/Dear-AI)
- **Issues:** Open an issue for bugs or feature requests
- **Discussions:** Ask questions in the GitHub Discussions tab

---

## 🙏 Acknowledgements

- **LangChain** — AI orchestration framework
- **Google Generative AI** — LLM and TTS capabilities
- **FastAPI** — Modern web framework
- **PostgreSQL** — Robust database solution
- **SSIP** — Project initiative

---

<div align="center">

**Made with ❤️ for mental health support**

If this project helps you, please consider giving it a ⭐ on GitHub!

</div>


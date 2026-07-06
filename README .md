# AI API Platform

A production-ready AI-powered REST API built with FastAPI and PostgreSQL. The platform provides secure user authentication, AI chat capabilities using Google's Gemini API, API key management, usage tracking, rate limiting, and chat history.

## Features

- User Registration & Login
- JWT Authentication
- Password Hashing (bcrypt)
- Gemini AI Chat API
- PostgreSQL Database
- SQLAlchemy ORM
- Chat History
- API Key Management
- Usage Tracking
- Rate Limiting
- Interactive Swagger Documentation
- Railway Deployment

## Tech Stack

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy
- JWT
- Gemini API
- Railway
- Uvicorn

## API Endpoints

### Authentication
- POST /register
- POST /login

### AI
- POST /chat

### User
- GET /me
- GET /profile

### Dashboard
- GET /dashboard

### History
- GET /history

### API Keys
- POST /generate-api-key
- GET /my-api-keys

## Run Locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## Deployment

Deployed on Railway.

## Future Improvements

- Docker
- GitHub Actions
- Password Reset
- Email Verification
- Redis
- Background Tasks
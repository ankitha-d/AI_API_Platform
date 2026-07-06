# AI API Platform
<img width="1672" height="941" alt="banner png" src="https://github.com/user-attachments/assets/426fe27b-aac5-4f23-b9f5-f39b1b0a4913" />


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
<img width="758" height="462" alt="swagger png" src="https://github.com/user-attachments/assets/3a08255a-ac57-46b9-9364-7008a8fcf8e5" />

### Authentication
- POST /register
- POST /login

### AI
<img width="583" height="427" alt="chat png" src="https://github.com/user-attachments/assets/fe043557-0d4e-436b-b172-ceb204a19543" />

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
<img width="920" height="458" alt="railway png" src="https://github.com/user-attachments/assets/7fcf7a30-8f13-4fb4-8a60-d6b01c0042e4" />

Deployed on Railway.

## Future Improvements

- Docker
- GitHub Actions
- Password Reset
- Email Verification
- Redis
- Background Tasks

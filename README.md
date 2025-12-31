# Job Listing & Candidate Matching Microservice

A Python microservice for managing job postings, candidate profiles, and computing top K candidate matches using TF-IDF text similarity.

## Features

- Create and retrieve job postings
- Create and retrieve candidate profiles  
- Compute top K candidate matches for any job using TF-IDF cosine similarity
- SQLite persistence
- RESTful JSON API

## Installation

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the Server

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

The database will be automatically initialized on first startup.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/jobs` | Create a job posting |
| GET | `/jobs` | List all jobs |
| GET | `/jobs/{job_id}` | Get a specific job |
| POST | `/candidates` | Create a candidate profile |
| GET | `/candidates` | List all candidates |
| GET | `/candidates/{cand_id}` | Get a specific candidate |
| GET | `/jobs/{job_id}/matches?top_k=K` | Get top K matching candidates |
| GET | `/health` | Health check |

## Example Usage

### Create Jobs

```bash
# Create a Python Developer job
curl -X POST http://localhost:8000/jobs \
  -H "Content-Type: application/json" \
  -d '{"title": "Senior Python Developer", "description": "Build scalable backend services using Python and FastAPI", "requirements": "5+ years Python, FastAPI, SQLAlchemy, PostgreSQL"}'

# Create a Data Scientist job
curl -X POST http://localhost:8000/jobs \
  -H "Content-Type: application/json" \
  -d '{"title": "Data Scientist", "description": "Analyze data and build ML models for product recommendations", "requirements": "Python, scikit-learn, TensorFlow, SQL"}'

# Create a Frontend Developer job
curl -X POST http://localhost:8000/jobs \
  -H "Content-Type: application/json" \
  -d '{"title": "Frontend Developer", "description": "Build responsive web applications using React", "requirements": "JavaScript, React, TypeScript, CSS"}'
```

### Create Candidates

```bash
# Candidate 1 - Python Backend Developer
curl -X POST http://localhost:8000/candidates \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice Johnson", "skills": "Python, FastAPI, Django, PostgreSQL, Docker", "summary": "Experienced backend developer with 7 years building scalable APIs"}'

# Candidate 2 - Data Scientist
curl -X POST http://localhost:8000/candidates \
  -H "Content-Type: application/json" \
  -d '{"name": "Bob Smith", "skills": "Python, scikit-learn, TensorFlow, Pandas, SQL", "summary": "ML engineer specializing in recommendation systems and NLP"}'

# Candidate 3 - Full Stack Developer
curl -X POST http://localhost:8000/candidates \
  -H "Content-Type: application/json" \
  -d '{"name": "Carol Williams", "skills": "JavaScript, React, Node.js, Python, MongoDB", "summary": "Full stack developer with frontend focus"}'

# Candidate 4 - Junior Python Developer
curl -X POST http://localhost:8000/candidates \
  -H "Content-Type: application/json" \
  -d '{"name": "David Lee", "skills": "Python, Flask, MySQL, Git", "summary": "Python developer with 2 years experience in web development"}'

# Candidate 5 - Frontend Specialist
curl -X POST http://localhost:8000/candidates \
  -H "Content-Type: application/json" \
  -d '{"name": "Eva Martinez", "skills": "JavaScript, TypeScript, React, Vue, CSS, HTML", "summary": "Frontend specialist creating beautiful responsive UIs"}'
```

### List All Jobs and Candidates

```bash
# Get all jobs
curl http://localhost:8000/jobs

# Get all candidates
curl http://localhost:8000/candidates
```

### Get Job Matches

```bash
# Get top 5 matches for a job (replace JOB_ID with actual ID from /jobs)
curl "http://localhost:8000/jobs/{JOB_ID}/matches?top_k=5"

# Get top 3 matches
curl "http://localhost:8000/jobs/{JOB_ID}/matches?top_k=3"
```

## API Documentation

Interactive API documentation available at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
├── app.py          # FastAPI application & endpoints
├── models.py       # SQLAlchemy database models
├── schemas.py      # Pydantic request/response schemas
├── crud.py         # Database CRUD operations
├── matching.py     # TF-IDF matching logic
├── docs/           # Developer documentation
├── requirements.txt
└── README.md
```

## Learning the Codebase

- Codebase learning guide: `docs/CODEBASE_LEARNING.md`

## Docker

### Build and Run with Docker

```bash
# Build the image
docker build -t candidate-matching .

# Run the container
docker run -p 8000:8000 candidate-matching
```

The API will be available at http://localhost:8000

### Docker Compose (optional)

```bash
docker-compose up --build
```

## Tech Stack

- **Framework**: FastAPI
- **Database**: SQLite with SQLAlchemy ORM
- **ML**: scikit-learn (TF-IDF, cosine similarity)
- **Validation**: Pydantic

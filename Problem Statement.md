Problem Statement
Design and implement a job-listing and candidate-matching microservice in Python. The service must allow clients to create and retrieve job postings and candidate profiles, and to compute the top K candidate matches for any given job based on text similarity of job descriptions vs. candidate summaries. You will deliver a working REST API, persistence layer, matching logic, and a brief README demonstrating usage.

Key Deliverables

Data Models & Persistence

Job Posting:
• id (UUID or auto-increment)
• title (string, required)
• description (text, required)
• requirements (text, optional)
Candidate Profile:
• id (UUID or auto-increment)
• name (string, required)
• skills (text, comma-separated or JSON array, required)
• summary (text, optional)
Store all records in a local SQLite database. Use SQLAlchemy or Python’s built-in sqlite3.
REST API Endpoints (JSON over HTTP)

POST /jobs
• Request body: JSON with title, description, requirements
• Response: created job object (including id)
GET /jobs
• Response: list of all job objects
GET /jobs/{job_id}
• Response: the job object with given id or 404 if not found
POST /candidates
• Request body: JSON with name, skills, summary
• Response: created candidate object (including id)
GET /candidates
• Response: list of all candidate objects
GET /candidates/{cand_id}
• Response: the candidate object with given id or 404 if not found
GET /jobs/{job_id}/matches?top_k=K
• Query param: top_k (integer, default 5)
• Response: JSON array of top K candidate objects sorted by similarity score, each with {candidate_id, name, score}.
Matching Logic

Use scikit-learn’s TfidfVectorizer to vectorize the concatenated text of each candidate (skills + summary) and the concatenated text of each job (title + description + requirements).
At query time, compute cosine similarity between the vector for the requested job and all candidate vectors.
Return the top K candidates with highest scores (descending).
Technical Requirements

Python 3.8+
FastAPI (or Flask if you prefer) for the HTTP API
scikit-learn for TF-IDF and cosine similarity
SQLAlchemy or sqlite3 for persistence
Pydantic (if FastAPI) or Marshmallow for request/response validation
Include error handling: 400 for invalid input, 404 for missing records, 500 for internal errors
Project Structure & Documentation

A README.md that describes:
• How to install dependencies (requirements.txt or pyproject.toml)
• How to initialize the database
• How to start the server
• Example curl or HTTPie commands for each endpoint
A main application file (e.g., app.py), modules for models, schemas, and matching logic
(Optional) Dockerfile to containerize the service
Success Criteria

You can start the service in under 2 minutes following your README.
You can add at least 3 jobs and 5 candidates via the API, then retrieve matches for one job, and see reasonable similarity‐based ordering.
Code is clear, modular, and demonstrates best practices in API design and Python.
"""FastAPI application for Job Listing and Candidate Matching service."""
from typing import List
from fastapi import FastAPI, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from models import init_db, get_db
from schemas import (
    JobCreate, JobResponse,
    CandidateCreate, CandidateResponse,
    MatchResult
)
import crud
from matching import compute_matches

# Initialize FastAPI app
app = FastAPI(
    title="Job Listing & Candidate Matching API",
    description="A microservice for managing job postings, candidate profiles, and computing top K candidate matches",
    version="1.0.0"
)


@app.on_event("startup")
def startup_event():
    """Initialize database on startup."""
    init_db()


# Job Endpoints
@app.post("/jobs", response_model=JobResponse, status_code=201)
def create_job(job: JobCreate, db: Session = Depends(get_db)):
    """Create a new job posting."""
    return crud.create_job(db, job)


@app.get("/jobs", response_model=List[JobResponse])
def list_jobs(db: Session = Depends(get_db)):
    """Get all job postings."""
    return crud.get_jobs(db)


@app.get("/jobs/{job_id}", response_model=JobResponse)
def get_job(job_id: str, db: Session = Depends(get_db)):
    """Get a job posting by ID."""
    job = crud.get_job(db, job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    return job


# Candidate Endpoints
@app.post("/candidates", response_model=CandidateResponse, status_code=201)
def create_candidate(candidate: CandidateCreate, db: Session = Depends(get_db)):
    """Create a new candidate profile."""
    return crud.create_candidate(db, candidate)


@app.get("/candidates", response_model=List[CandidateResponse])
def list_candidates(db: Session = Depends(get_db)):
    """Get all candidate profiles."""
    return crud.get_candidates(db)


@app.get("/candidates/{cand_id}", response_model=CandidateResponse)
def get_candidate(cand_id: str, db: Session = Depends(get_db)):
    """Get a candidate profile by ID."""
    candidate = crud.get_candidate(db, cand_id)
    if candidate is None:
        raise HTTPException(status_code=404, detail="Candidate not found")
    return candidate


# Matching Endpoint
@app.get("/jobs/{job_id}/matches", response_model=List[MatchResult])
def get_job_matches(
    job_id: str,
    top_k: int = Query(default=5, ge=1, le=100, description="Number of top matches to return"),
    db: Session = Depends(get_db)
):
    """
    Get top K candidate matches for a job based on TF-IDF similarity.
    
    Returns candidates sorted by similarity score (descending).
    """
    # Verify job exists
    job = crud.get_job(db, job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")
    
    # Get all candidates
    candidates = crud.get_candidates(db)
    if not candidates:
        return []
    
    # Compute matches
    matches = compute_matches(job, candidates, top_k)
    
    # Format response
    return [
        MatchResult(
            candidate_id=candidate.id,
            name=candidate.name,
            score=round(score, 4)
        )
        for candidate, score in matches
    ]


# Health check endpoint
@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


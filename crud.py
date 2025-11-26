"""CRUD operations for Jobs and Candidates."""
from typing import List, Optional
from sqlalchemy.orm import Session
from models import Job, Candidate
from schemas import JobCreate, CandidateCreate


# Job CRUD operations
def create_job(db: Session, job: JobCreate) -> Job:
    """Create a new job posting."""
    db_job = Job(
        title=job.title,
        description=job.description,
        requirements=job.requirements
    )
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def get_jobs(db: Session) -> List[Job]:
    """Get all job postings."""
    return db.query(Job).all()


def get_job(db: Session, job_id: str) -> Optional[Job]:
    """Get a job posting by ID."""
    return db.query(Job).filter(Job.id == job_id).first()


# Candidate CRUD operations
def create_candidate(db: Session, candidate: CandidateCreate) -> Candidate:
    """Create a new candidate profile."""
    db_candidate = Candidate(
        name=candidate.name,
        skills=candidate.skills,
        summary=candidate.summary
    )
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate


def get_candidates(db: Session) -> List[Candidate]:
    """Get all candidate profiles."""
    return db.query(Candidate).all()


def get_candidate(db: Session, candidate_id: str) -> Optional[Candidate]:
    """Get a candidate profile by ID."""
    return db.query(Candidate).filter(Candidate.id == candidate_id).first()


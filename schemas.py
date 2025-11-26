"""Pydantic schemas for request/response validation."""
from typing import Optional, List
from pydantic import BaseModel, Field


# Job Schemas
class JobCreate(BaseModel):
    """Schema for creating a job posting."""
    title: str = Field(..., min_length=1, description="Job title")
    description: str = Field(..., min_length=1, description="Job description")
    requirements: Optional[str] = Field(None, description="Job requirements")


class JobResponse(BaseModel):
    """Schema for job response."""
    id: str
    title: str
    description: str
    requirements: Optional[str] = None

    class Config:
        from_attributes = True


# Candidate Schemas
class CandidateCreate(BaseModel):
    """Schema for creating a candidate profile."""
    name: str = Field(..., min_length=1, description="Candidate name")
    skills: str = Field(..., min_length=1, description="Comma-separated skills or JSON array")
    summary: Optional[str] = Field(None, description="Candidate summary")


class CandidateResponse(BaseModel):
    """Schema for candidate response."""
    id: str
    name: str
    skills: str
    summary: Optional[str] = None

    class Config:
        from_attributes = True


# Match Schemas
class MatchResult(BaseModel):
    """Schema for a single match result."""
    candidate_id: str
    name: str
    score: float = Field(..., description="Similarity score between 0 and 1")


class MatchListResponse(BaseModel):
    """Schema for list of match results."""
    matches: List[MatchResult]


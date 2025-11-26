"""Matching logic using TF-IDF and cosine similarity."""
from typing import List, Tuple
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from models import Job, Candidate


def get_job_text(job: Job) -> str:
    """Concatenate job text fields for vectorization."""
    parts = [job.title, job.description]
    if job.requirements:
        parts.append(job.requirements)
    return " ".join(parts)


def get_candidate_text(candidate: Candidate) -> str:
    """Concatenate candidate text fields for vectorization."""
    parts = [candidate.skills]
    if candidate.summary:
        parts.append(candidate.summary)
    return " ".join(parts)


def compute_matches(job: Job, candidates: List[Candidate], top_k: int = 5) -> List[Tuple[Candidate, float]]:
    """
    Compute top K candidate matches for a job based on TF-IDF cosine similarity.
    
    Args:
        job: The job posting to match against
        candidates: List of candidate profiles
        top_k: Number of top matches to return (default 5)
    
    Returns:
        List of tuples (Candidate, similarity_score) sorted by score descending
    """
    if not candidates:
        return []
    
    # Prepare texts for vectorization
    job_text = get_job_text(job)
    candidate_texts = [get_candidate_text(c) for c in candidates]
    
    # Combine all texts for TF-IDF fitting
    all_texts = [job_text] + candidate_texts
    
    # Create TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    
    # Job vector is the first row, candidate vectors are the rest
    job_vector = tfidf_matrix[0:1]
    candidate_vectors = tfidf_matrix[1:]
    
    # Compute cosine similarity between job and all candidates
    similarities = cosine_similarity(job_vector, candidate_vectors).flatten()
    
    # Create list of (candidate, score) pairs
    candidate_scores = list(zip(candidates, similarities))
    
    # Sort by score descending and take top K
    candidate_scores.sort(key=lambda x: x[1], reverse=True)
    
    return candidate_scores[:top_k]


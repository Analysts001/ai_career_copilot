from embeddings import get_embedding
import numpy as np

job_database = [
    "Python Developer with ML knowledge",
    "Data Scientist with NLP experience",
    "Backend Developer with API skills"
]

def find_best_match(resume_text):
    resume_vec = get_embedding(resume_text)

    best_match = None
    best_score = -1

    for job in job_database:
        job_vec = get_embedding(job)

        score = np.dot(resume_vec, job_vec)

        if score > best_score:
            best_score = score
            best_match = job

    return {
        "best_match": best_match,
        "score": float(best_score)
    }
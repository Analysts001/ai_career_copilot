def job_match_prompt(resume, job_desc):
    return f"""
    You are an AI recruiter.

    Analyze the resume against job description.

    Return:
    - Match Score (0-100)
    - Matching Skills
    - Missing Skills
    - Suggestions to improve

    Resume:
    {resume}

    Job Description:
    {job_desc}
    """
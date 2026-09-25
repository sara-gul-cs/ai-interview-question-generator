import pandas as pd
import re

# ============================================================
# 1. LOAD THE QUESTION BANK
# ============================================================
df = pd.read_csv('question_bank.csv')
print(f"Loaded question bank with {len(df)} questions across "
      f"{df['skill_tag'].nunique()} skill areas.\n")

# ============================================================
# 2. MATCH JOB DESCRIPTION -> RELEVANT SKILLS
# ============================================================
# This is a simple keyword-matching approach: it scans the job description
# for known skill keywords and pulls matching technical questions, plus a
# fixed set of behavioral questions every interview should include.
def extract_skills(job_description, known_skills):
    job_description_lower = job_description.lower()
    matched = [skill for skill in known_skills if skill in job_description_lower]
    return matched

def generate_interview_questions(job_description, intern_name="Candidate",
                                   n_technical=4, n_behavioral=3):
    known_skills = df[df['category'] == 'technical']['skill_tag'].unique().tolist()
    matched_skills = extract_skills(job_description, known_skills)

    if not matched_skills:
        matched_skills = ['python']  # sensible default if nothing matches
        print("No specific skills matched in job description - defaulting to Python questions.")

    # Pull technical questions for matched skills
    technical_pool = df[(df['category'] == 'technical') & (df['skill_tag'].isin(matched_skills))]
    technical_questions = technical_pool['question'].sample(
        n=min(n_technical, len(technical_pool)), random_state=42
    ).tolist()

    # Pull behavioral questions (always relevant, regardless of role)
    behavioral_pool = df[df['category'] == 'behavioral']
    behavioral_questions = behavioral_pool['question'].sample(
        n=min(n_behavioral, len(behavioral_pool)), random_state=42
    ).tolist()

    return {
        'candidate': intern_name,
        'matched_skills': matched_skills,
        'technical_questions': technical_questions,
        'behavioral_questions': behavioral_questions
    }

# ============================================================
# 3. TEST ON TWO DIFFERENT JOB DESCRIPTIONS
# ============================================================
job_description_1 = """
We are looking for a Machine Learning Intern with strong Python skills.
The candidate should be comfortable with data analysis and building models.
"""

job_description_2 = """
Looking for a Web Development Intern experienced with SQL and building
scalable applications in the cloud.
"""

for i, jd in enumerate([job_description_1, job_description_2], start=1):
    print(f"\n{'='*60}")
    print(f"Job Description {i}: {jd.strip()[:70]}...")
    print('='*60)
    result = generate_interview_questions(jd, intern_name=f"Candidate_{i}")
    print(f"Matched skills: {result['matched_skills']}")
    print("\nTechnical Questions:")
    for q in result['technical_questions']:
        print(f"  - {q}")
    print("\nBehavioral Questions:")
    for q in result['behavioral_questions']:
        print(f"  - {q}")

# OPTIONAL: True LLM-generated version using OpenAI's GPT API.
# This is closer to what the task guidelines describe ("Model Type: GPT-3"),
# but requires an OpenAI account with a linked payment method (this task
# costs only a few cents to run). If you don't have one, the template-based
# version (interview_question_generator.py) is a fully legitimate, free
# alternative that achieves the same outcome.
#
# Setup:
#   1. pip install openai
#   2. Get an API key from https://platform.openai.com/api-keys
#   3. Set it as an environment variable (recommended, keeps it out of your code):
#        Mac/Linux: export OPENAI_API_KEY="your-key-here"
#        Windows:   setx OPENAI_API_KEY "your-key-here"

import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_questions_with_gpt(job_description, n_technical=4, n_behavioral=3):
    prompt = f"""You are an interview coach helping design an intern interview.
Job description: {job_description}

Generate {n_technical} technical interview questions specific to the skills
mentioned in the job description, and {n_behavioral} general behavioral
interview questions suitable for an intern-level candidate.

Format your response as:
TECHNICAL:
1. ...
BEHAVIORAL:
1. ...
"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    job_description = """
    We are looking for a Machine Learning Intern with strong Python skills.
    The candidate should be comfortable with data analysis and building models.
    """
    result = generate_questions_with_gpt(job_description)
    print(result)

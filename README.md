# AI-Powered Interview Question Generator

Objective :
Generate custom technical and behavioral interview questions for intern
candidates, based on a job description.

Approach: Two versions provided

### 1. Template-based version (`interview_question_generator.py`) — FREE, no API key needed
- Built a tagged question bank (21 questions across 8 skill areas: Python,
  Machine Learning, SQL, Web Development, Data Analysis, NLP, Cloud
  Computing, plus general behavioral questions).
- The generator scans a job description for skill keywords, then pulls
  matching technical questions and a fixed set of behavioral questions.
- This is a legitimate, rule-based automation approach to the stated
  outcome ("automated, role-specific interview question sets"), and runs
  immediately with no setup beyond `pip install pandas`.

### 2. GPT-powered version (`interview_question_generator_gpt_optional.py`) — requires OpenAI API key
- Uses OpenAI's GPT model to generate genuinely novel questions from the
  job description text, rather than selecting from a fixed bank.
- Closer to what the task guidelines describe (Model Type: GPT-3/LLaMA).
- Requires an OpenAI account with a linked payment method — cost for
  running this task is a few cents, not free.

## Why two versions
The template-based version is included as a fully working, zero-cost
solution that meets the task's outcome. The GPT version is included to
show understanding of the "true" LLM-based approach guidelines describe,
for anyone who wants to extend this with a paid API key.

## Results (template-based version)
Tested on two different job descriptions:

**Job Description 1** (Machine Learning Intern, Python):
- Matched skills: python, machine learning, data analysis
- Sample technical question: "How does Python handle memory management?"
- Sample behavioral question: "Describe a situation where you had to learn
  a new skill quickly."

**Job Description 2** (Web Development Intern, SQL):
- Matched skills: sql, web development
- Sample technical question: "Explain the difference between INNER JOIN
  and LEFT JOIN."

Different job descriptions correctly produced different, relevant question sets.

## Limitation 
The template-based version only returns from a fixed, hand-built bank of
21 questions — it can't generate a genuinely new question it hasn't seen
before. This is a rule-based automation, not true text generation. The
GPT version solves this by generating novel text, at the cost of requiring
a paid API key.

## Files
- `question_bank.csv` — tagged bank of technical + behavioral questions
- `interview_question_generator.py` — free, template-based generator (run this one)
- `interview_question_generator_gpt_optional.py` — optional GPT-powered version
- `README.md` — this file

## How to run
```
pip install pandas
python3 interview_question_generator.py
```

To try the GPT version instead (optional, needs an API key):
```
pip install openai
export OPENAI_API_KEY="your-key-here"
python3 interview_question_generator_gpt_optional.py
```

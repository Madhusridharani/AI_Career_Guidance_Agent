import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def get_career_guidance(student):

    prompt = f"""
You are an AI Career Guidance Expert.

Student Details:
- Academic Percentage: {student['percentage']}
- Programming: {student['programming']}
- Mathematics: {student['maths']}
- Communication: {student['communication']}
- Leadership: {student['leadership']}
- Creativity: {student['creativity']}
- Personality: {student['personality']}

Provide:
1. Best Career
2. Why this career suits the student
3. Skills to learn
4. 6-month learning roadmap
5. Certifications
6. Salary range
7. Top hiring companies

Format the answer in Markdown.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
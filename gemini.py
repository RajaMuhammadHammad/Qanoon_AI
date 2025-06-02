import google.generativeai as genai
from config import GEMINI_API_KEY

genai.configure(api_key=GEMINI_API_KEY)
gemini_model = genai.GenerativeModel('gemini-2.0-flash')

def generate_answer(full_prompt):
    response = gemini_model.generate_content(full_prompt)
    return response.text.strip()

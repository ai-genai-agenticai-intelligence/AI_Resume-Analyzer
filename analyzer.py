import ollama
from prompts import PROMPT

def analyze_resume(resume_text):
    prompt_text = PROMPT.format(resume=resume_text)

    response = ollama.chat(
        model="qwen2.5:3b",
        messages=[{"role": "user", "content": prompt_text}])

    return response["message"]["content"]

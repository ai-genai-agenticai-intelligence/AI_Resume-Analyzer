import os

import streamlit as st
from huggingface_hub import InferenceClient

from prompts import PROMPT

MODEL_NAME = "Qwen/Qwen2.5-7B-Instruct"


def _get_huggingface_token():
    token = os.getenv("HF_TOKEN")
    if token:
        return token

    try:
        return st.secrets["HF_TOKEN"]
    except (KeyError, FileNotFoundError):
        return None


def analyze_resume(resume_text):
    token = _get_huggingface_token()
    if not token:
        raise RuntimeError(
            "HF_TOKEN is not configured. Add your Hugging Face token in "
            "Streamlit Cloud under Settings > Secrets."
        )

    prompt_text = PROMPT.format(resume=resume_text)
    client = InferenceClient(model=MODEL_NAME, token=token)
    response = client.chat_completion(
        messages=[{"role": "user", "content": prompt_text}],
        max_tokens=1800,
        temperature=0.2,
    )
    return response.choices[0].message.content

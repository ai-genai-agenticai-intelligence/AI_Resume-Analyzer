# AI Resume Analyzer

This Streamlit app extracts text from a PDF resume and analyzes it with the
hosted `Qwen/Qwen2.5-7B-Instruct` model through Hugging Face Inference.

## Streamlit Cloud setup

1. Create a Hugging Face access token with inference permissions.
2. Open the deployed app's **Settings > Secrets**.
3. Add:

```toml
HF_TOKEN = "hf_your_token_here"
```

The app no longer requires a local Ollama server, which is unavailable inside
Streamlit Cloud.

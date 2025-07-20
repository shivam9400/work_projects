import os
from dotenv import load_dotenv

USE_STREAMLIT_SECRETS = False

try:
    import streamlit as st
    if st._is_running_with_streamlit:
        USE_STREAMLIT_SECRETS = True
except (ImportError, AttributeError):
    st = None  # fallback if streamlit is not available

# Absolute path to .env file
env_path = os.path.join(os.path.dirname(__file__), ".env")

# Load .env only if NOT using Streamlit secrets
if not USE_STREAMLIT_SECRETS:
    load_dotenv(dotenv_path=env_path)

def get_secret(key: str, default: str = None) -> str:
    """
    Fetch secrets from Streamlit if running inside Streamlit app,
    otherwise from environment variables.
    """
    if USE_STREAMLIT_SECRETS:
        return st.secrets.get(key, default)
    return os.getenv(key, default)

# Now fetch secrets through this function
MONGO_DB_URI = get_secret("MONGO_DB_URI")
MONGO_COLLECTION = get_secret("MONGO_COLLECTION", "embedded_chunks")
HF_TOKEN = get_secret("HF_API_TOKEN")
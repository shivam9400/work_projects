import os
from dotenv import load_dotenv

try:
    import streamlit as st
    # Detect if secrets are usable (Cloud or local TOML present)
    # Avoid touching st.secrets directly to prevent StreamlitSecretNotFoundError
    secrets_available = False
    try:
        _ = st.secrets["HF_API_TOKEN"]  # try to access one required secret
        secrets_available = True
    except Exception:
        pass
except ImportError:
    st = None
    secrets_available = False

# Load .env only if Streamlit secrets are not available
if not secrets_available:
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(dotenv_path=env_path)

def get_secret(key: str, default: str = None) -> str:
    if secrets_available:
        return st.secrets.get(key, default)
    return os.getenv(key, default)

# Access secrets safely
MONGO_DB_URI = get_secret("MONGO_DB_URI")
MONGO_COLLECTION = get_secret("MONGO_COLLECTION", "embedded_chunks")
HF_TOKEN = get_secret("HF_API_TOKEN")
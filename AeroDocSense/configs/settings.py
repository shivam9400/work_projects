import os
from dotenv import load_dotenv

try:
    import streamlit as st
    from streamlit.runtime.scriptrunner import get_script_run_ctx
    USE_STREAMLIT_SECRETS = get_script_run_ctx() is not None
except ImportError:
    st = None
    USE_STREAMLIT_SECRETS = False



if not USE_STREAMLIT_SECRETS:
    env_path = os.path.join(os.path.dirname(__file__), ".env")
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
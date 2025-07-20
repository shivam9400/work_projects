from dotenv import load_dotenv
from pydantic_settings import BaseSettings
import os

# Load .env file from the expected path
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), ".env"))

class Settings(BaseSettings):
    MONGO_DB_URI: str
    MONGO_DB_NAME: str = "aerodocsense_db"
    MONGO_COLLECTION: str = "embedded_chunks"
    HF_TOKEN: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
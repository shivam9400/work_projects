from pymongo import MongoClient
import os
from dotenv import load_dotenv
from configs import settings

class MongoDBHandler:
    def __init__(self, db_name="aerodocsense_db", collection_name="embedded_chunks"):
        mongo_uri = settings.MONGO_DB_URI
        if not mongo_uri:
            raise ValueError("MONGO_DB_URI not found in environment variables")
        
        # Added TLS options for compatibility with Streamlit Cloud
        self.client = MongoClient(
            mongo_uri,
            tls=True,
            tlsAllowInvalidCertificates=True  # Only use for testing!
        )
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_many(self, documents):
        """
        Insert multiple documents (each should be a dict).
        """
        if documents:
            self.collection.insert_many(documents)
        else:
            print("[WARNING] Empty document list passed to insert_many.")
    
    def find_all(self):
        """
        Return all documents in collection.
        """
        return list(self.collection.find({}))
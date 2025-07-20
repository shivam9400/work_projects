import streamlit as st
st.write("App Started!")


# from app.generate import answer_query
# import streamlit as st
# from configs import settings


# HF_TOKEN = settings.HF_TOKEN
# MONGO_URI = settings.MONGO_DB_URI

# st.write("HF_TOKEN loaded?", HF_TOKEN is not None)
# st.write("Mongo URI:", MONGO_URI)

# st.set_page_config(page_title="AeroDocSense", layout="centered")

# st.title("AeroDocSense - RAG for Aircraft hydraulic systems")
# st.markdown("Ask a question based on ATA 29")

# query = st.text_input("Enter your query", placeholder="e.g., What are maintenance procedures for A320 engines?")

# if st.button("Generate Answer"):
#     if query.strip():
#         with st.spinner("Generating answer..."):
#             response = answer_query(query)
#             st.success(response)
#     else:
#         st.warning("Please enter a query.")
# AeroDocSense: Sensing Relevance in Aerospace Maintenance Documents ✈️🧠

**AeroDocSense** is an AI-powered Retrieval-Augmented Generation (RAG) system designed to assist aerospace maintenance engineers in efficiently querying and interpreting complex maintenance documents using natural language. 

---

## Problem Statement

Modern aircraft systems such as the **hydraulic system** are critical to safe operations, powering:
- Landing gear extension and retraction
- Flight control surfaces like rudder, aileron, and elevator
- Brakes and steering

Maintenance of such systems requires combing through numerous **disparate documents** like:
- OEM Manuals (AMM, IPC)
- Service Bulletins (SB)
- Maintenance Logs
- Fault Isolation Reports
- Regulatory Compliance Docs
- Troubleshooting Guides

### Current Challenges
- Scattered documentation in varied formats (PDFs, Excel sheets, handwritten notes)
- Search tools often rely on **basic keyword matching**
- Lack of semantic understanding can lead to **delays and costly errors**

---

## Solution with RAG

AeroDocSense leverages a **Retrieval-Augmented Generation** (RAG) pipeline to enable:
- Natural language queries from technicians and engineers
- Retrieval of **context-rich document chunks** using vector similarity
- Summarized answers with **source-grounded recommendations**

---

## Example Use Case

A technician in Pune is troubleshooting a **hydraulic leak** in the left main gear of an **Airbus A320** and inputs:

> “How do I identify the source of a hydraulic leak in the A320 main gear?”

AeroDocSense will:
1. **Embed the query**
2. **Search** relevant documentation chunks (e.g., ATA 29 – Hydraulic Power)
3. **Retrieve** inspection steps or fault isolation procedures
4. **Generate** a human-like summary with referenced sources

---
## How It Works

1. **Document Ingestion** (`ingest.py`)
   - Loads documents from `data/sample_docs/`
   - Splits text into overlapping chunks
   - Embeds each chunk using a sentence transformer
   - Stores the embeddings in a **MongoDB** collection

2. **Query Processing** (`inference.py` or Streamlit UI)
   - User enters a natural language query
   - Query is embedded and matched against the vector DB
   - Top `k` relevant chunks are retrieved
   - A local LLM or remote API generates a final answer using the retrieved context

---

## Folder Structure

```bash
AeroDocSense/
│
├── app/
│   ├── main.py                  # Streamlit app entry point
│   ├── search.py                # Document retrieval logic
│   ├── generate.py              # LLM-based answer generation
│   └── models/
│       ├── request_models.py    # Pydantic models for API input
│       └── response_models.py   # Pydantic models for API output
│
├── utils/
│   ├── chunker.py               # Splits documents into chunks
│   ├── embedder.py              # Embeds text using HuggingFace models
│   ├── llm_client.py            # Connects to LLM for generation
│   ├── prompt_engine.py         # Prompt templates and engineering
│   └── mongo_handler.py         # MongoDB interaction logic
│
├── configs/
│   ├── settings.py              # Environment and secrets config
│   └── .env                     # Local secrets (ignored in GitHub)
│
├── data/
│   └── sample_docs/             # Sample input documents (PDF, txt)
│
├── ingest.py                    # Loads and embeds documents into DB
├── inference.py                 # Query and inference script (CLI)
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---
## Configuration (Secrets)

Secrets are handled via a hybrid approach using `.env` and `streamlit.secrets`.
---

## Setting Up the Project
1. Clone the repository
```bash
git clone https://github.com/your-username/AeroDocSense.git
cd AeroDocSense
```
2. Create virtual environment 
```bash
python -m venv venv
source venv\Scripts\activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Set up .env file inside configs/
```bash
MONGO_DB_URI=mongodb://localhost:27017
MONGO_COLLECTION=embedded_chunks
HF_API_TOKEN=your_huggingface_api_key
```
5. Ingest documents
```bash
python ingest.py
```
6. Run inference
```bash
python inference.py
```
---
## Future Scope
1. Expand to other systems beyond hydraulics (e.g., electrical, pneumatic, ECS)
2. Support for multimodal inputs (PDFs, diagrams, images)
3. Feedback-based improvement via technician interactions
4. Fine-tuning the model on real-world maintenance reports
5. Intelligent clustering of similar fault reports for RCA
---
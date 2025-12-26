# Module Extraction AI Agent

## Description
This project is an AI-powered system that extracts structured modules and submodules from documentation-based help websites. It converts unstructured documentation content into a clean, deduplicated JSON format that can be used by product and engineering teams.

The system combines semantic extraction using a local Large Language Model (LLM) with deterministic post-processing to ensure consistency and accuracy.

## Features
- Crawls documentation URLs
- Cleans and normalizes HTML content
- Extracts product modules and submodules using AI
- Deduplicates overlapping topics
- Outputs structured JSON
- Includes a Streamlit-based demo UI
- Runs fully locally without API keys

## Tech Stack
- Python 3.10
- LangChain
- Ollama (LLaMA 3)
- Requests
- BeautifulSoup
- Streamlit
- Git and GitHub

## Project Structure
module_extractor/
├── ai/
├── crawler/
├── output/
├── app.py
├── test_ai.py
├── test_parser.py
├── .gitignore
└── README.md

## How to Run
python -m venv env
.\env\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app.py

## Sample Output
[
  {
    "module": "Technical Guides",
    "Description": "Technical documentation for setup, maintenance, and security.",
    "Submodules": {
      "Installation": "Instructions to install WordPress.",
      "Maintenance": "Keeping WordPress updated and healthy.",
      "Security": "Best practices to protect WordPress sites."
    }
  }
]

## Design Notes
- Uses LLM-based semantic understanding for accurate extraction
- Applies deterministic logic for deduplication
- Produces a flat, product-level module structure
- Designed to be simple, scalable, and interview-ready

## Author
Sri Krishna  
GitHub: https://github.com/sri-krishna-c

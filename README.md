Module Extraction AI Agent
Overview

The Module Extraction AI Agent is an AI-powered system designed to extract structured modules and submodules from documentation-based help websites.
It converts unstructured documentation into a clean, deduplicated, and stakeholder-ready JSON format, enabling clear product understanding and analysis.

This project combines semantic extraction using Large Language Models (LLMs) with deterministic post-processing to ensure accuracy, consistency, and scalability.

Objectives

Crawl and process documentation URLs

Extract high-level product modules and submodules

Deduplicate and normalize overlapping topics

Generate structured JSON output

Provide an interactive demonstration interface

Key Features

Automated documentation crawling

HTML content cleaning and normalization

Semantic module extraction using a local LLM (Ollama – LLaMA 3)

Deduplication and topic consolidation

Structured, readable JSON output

Streamlit-based interactive UI

Fully local execution (no external API keys required)

Technology Stack

Programming Language : Python 3.10

AI / NLP : LangChain, Ollama (LLaMA 3)

Web Scraping : Requests, BeautifulSoup

User Interface : Streamlit

Version Control : Git, GitHub

Project Structure
module_extractor/
│
├── ai/
│   ├── module_extractor.py
│   ├── postprocess.py
│   └── final_formatter.py
│
├── crawler/
│   ├── fetcher.py
│   └── parser.py
│
├── output/
│   └── modules.json
│
├── app.py
├── test_ai.py
├── test_parser.py
├── .gitignore
└── README.md

Installation and Setup
Step 1: Clone the Repository
git clone https://github.com/sri-krishna-c/module-extraction-ai-agent.git
cd module-extraction-ai-agent

Step 2: Create and Activate Virtual Environment
python -m venv env
.\env\Scripts\Activate.ps1

Step 3: Install Dependencies
pip install -r requirements.txt

Step 4: Run the Application
streamlit run app.py

Usage

Launch the Streamlit application

Enter a documentation URL (e.g., WordPress documentation)

Click Extract Modules

View extracted modules and submodules in JSON format

Output is automatically saved to output/modules.json

Sample Output
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

Design Approach

LLM-based semantic extraction for contextual understanding

Deterministic post-processing for consistency and deduplication

Flat, normalized structure aligned with product-level expectations

Local LLM execution to eliminate API cost and dependency

Limitations

JavaScript-heavy documentation sites may require headless browsers

Output quality depends on the structure and clarity of documentation

Future Enhancements

Confidence scoring for extracted modules

Multi-URL batch processing

REST API support

Dockerized deployment

Support for additional documentation formats

Project Summary

This project demonstrates how unstructured documentation can be transformed into structured product intelligence using AI-based semantic extraction combined with deterministic engineering practices.

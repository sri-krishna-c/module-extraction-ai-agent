from langchain_ollama import OllamaLLM
import json

def extract_modules(clean_text: str):
    llm = OllamaLLM(
        model="llama3",
        temperature=0
    )

    prompt = f"""
    You are an AI system that extracts structured product documentation.

    STRICT RULES:
    - Output ONLY valid JSON
    - NO explanations
    - NO markdown
    - NO text outside JSON
    - Output must be a JSON ARRAY

    JSON FORMAT:
    [
      {{
        "module": "Module Name",
        "Description": "Brief factual description",
        "Submodules": {{
          "Submodule Name": "Description"
        }}
      }}
    ]

    Use ONLY the content below.

    CONTENT:
    {clean_text}
    """

    response = llm.invoke(prompt)

    # Ensure clean JSON output
    return json.loads(response)

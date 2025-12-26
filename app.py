import streamlit as st
import json
from crawler.fetcher import fetch_page
from crawler.parser import extract_clean_text
from ai.final_formatter import format_final_modules

st.set_page_config(page_title="Module Extraction AI", layout="wide")

st.title("📘 Module Extraction AI Agent")
st.write("Extracts structured modules and submodules from product documentation.")

url = st.text_input(
    "Enter documentation URL",
    value="https://wordpress.org/documentation/"
)

if st.button("Extract Modules"):
    with st.spinner("Processing documentation..."):
        html = fetch_page(url)
        clean_text = extract_clean_text(html)
        result = format_final_modules(clean_text)

        st.success("Extraction completed!")

        st.subheader("📦 Extracted Modules")
        st.json(result)

        with open("output/modules.json", "w", encoding="utf-8") as f:
            json.dump(result, f, indent=2)

        st.info("Result saved to output/modules.json")

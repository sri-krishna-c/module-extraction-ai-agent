from crawler.fetcher import fetch_page
from crawler.parser import extract_clean_text
from ai.final_formatter import format_final_modules
import json

url = "https://wordpress.org/documentation/"

html = fetch_page(url)
clean_text = extract_clean_text(html)

final_output = format_final_modules(clean_text)

with open("output/modules.json", "w", encoding="utf-8") as f:
    json.dump(final_output, f, indent=2)

print("Final output saved to output/modules.json")

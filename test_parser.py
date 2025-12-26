from crawler.fetcher import fetch_page
from crawler.parser import extract_clean_text

url = "https://wordpress.org/documentation/"

html = fetch_page(url)
clean_text = extract_clean_text(html)

print("Clean text length:", len(clean_text))
print(clean_text[:500])

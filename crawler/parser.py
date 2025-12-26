from bs4 import BeautifulSoup

def extract_clean_text(html: str) -> str:
    """
    Extract meaningful text from HTML by removing
    headers, footers, navigation, scripts, and styles.
    """
    soup = BeautifulSoup(html, "html.parser")

    # Remove unwanted sections
    for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
        tag.decompose()

    text = soup.get_text(separator=" ")
    clean_text = " ".join(text.split())

    return clean_text

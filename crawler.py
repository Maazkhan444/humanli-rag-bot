import requests
from bs4 import BeautifulSoup

def scrape_site(url):
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    for tag in soup(["script","style","nav","footer","header","noscript","aside"]):
        tag.decompose()
    title = soup.title.string if soup.title else ""
    text = soup.get_text(separator=" ")
    return text, {"source": url, "title": title}

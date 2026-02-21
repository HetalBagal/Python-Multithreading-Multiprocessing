import threading
import requests
from bs4 import BeautifulSoup

urls = [
    'https://www.example.com/',
    'https://books.toscrape.com/',
    'https://web-scraping.dev/products',
    'https://www.w3schools.com/html/html_examples.asp'
]

def fetch_content(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise error for bad status
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"Fetched {len(soup.text)} characters from {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")

threads = []

for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All web pages fetched successfully.")
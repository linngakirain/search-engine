import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

WEBSITE_URL = "https://quotes.toscrape.com"
POLITENESS = 6 # seconds

def crawl():
    docs = []
    doc_id = 0
    page = 1
    last_req = 0 # time of last request

    while True:
        url = urljoin(WEBSITE_URL, f"/page/{page}/")
        if time.time() - last_req < POLITENESS:
            time.sleep(POLITENESS - (time.time() - last_req)) # wait until 6 seconds since last request
        response = requests.get(url)
        response.raise_for_status()
        last_req = time.time()

        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
    
        # combine text, author, tags into one string
        page_text = ""
        for q in quotes:
            span = q.find('span', class_='text')
            if span:
                page_text += span.get_text(strip=True) + " "
            author = q.find('small', class_='author')
            if author:
                page_text += author.get_text(strip=True) + " "
            tags = q.find_all('a', class_='tag')
            for t in tags:
                page_text += t.get_text(strip=True) + " "

        docs.append([doc_id, url, page_text.strip()])
        doc_id += 1

        next_page = soup.find('li', class_='next')
        if not next_page: # no next page
            break
        page += 1

    return docs
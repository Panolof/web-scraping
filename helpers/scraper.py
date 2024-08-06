import requests
from bs4 import BeautifulSoup

def fetch_page(url, proxies=None, headers=None):
    response = requests.get(url, proxies=proxies, headers=headers)
    response.raise_for_status()
    return response.text

def parse_html(html):
    return BeautifulSoup(html, 'html.parser')

def extract_links(soup, selector):
    return [a['href'] for a in soup.select(selector) if 'href' in a.attrs]

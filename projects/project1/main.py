from helpers.scraper import fetch_page, parse_html, extract_links
from helpers.proxy import rotate_proxies
from helpers.utils import setup_logging, delay

def main():
    setup_logging()
    proxy_pool = rotate_proxies()
    url = "http://example.com"
    
    for _ in range(3):  # Example to scrape 3 times
        proxy = next(proxy_pool)
        html = fetch_page(url, proxies={"http": proxy, "https": proxy})
        soup = parse_html(html)
        links = extract_links(soup, "a")
        print(links)
        delay(2)

if __name__ == "__main__":
    main()

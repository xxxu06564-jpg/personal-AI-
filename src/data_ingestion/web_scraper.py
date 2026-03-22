import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, base_url):
        self.base_url = base_url
    
    def fetch_content(self, url):
        response = requests.get(url)
        return response.content if response.status_code == 200 else None
    
    def filter_urls(self, urls, keyword):
        return [url for url in urls if keyword in url]
    
    def extract_content(self, html_content):
        soup = BeautifulSoup(html_content, 'html.parser')
        return soup.get_text()  


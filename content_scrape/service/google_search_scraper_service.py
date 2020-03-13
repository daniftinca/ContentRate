import re

from bs4 import BeautifulSoup
from pip._vendor import requests

from content_scrape.service.content_scraper_service import ContentScraperService


class GoogleSearchScraperService:
    REGEX = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    def scrape_page(self, url):
        page = requests.get(url)
        page_content = page.content
        return BeautifulSoup(page_content, 'html.parser')

    def construct_url(self, query):
        return "https://www.google.com/search?q=" + query.replace(" ", "+")

    def get_search_result(self, query):
        soup = self.scrape_page(self.construct_url(query))

        links = []

        for item in soup.findAll("div", {"class": "ZINbbc xpd O9g5cc uUPGi"}):
            anchors = item.find_all('a')
            link = anchors[0].get('href')[7:]
            if re.match(self.REGEX, link):
                links.append(link)

        return links

from bs4 import BeautifulSoup
from pip._vendor import requests

from content_scrape.model.content import Content


class ContentScraperService:
    BLACKLIST = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head',
        'input',
        'script',
        'style',
        'footer',
        'aside'
    ]

    def scrape_page(self, url):
        page = requests.get(url)
        page_content = page.content
        return BeautifulSoup(page_content, 'html.parser')

    def get_page_content(self, url):
        soup = self.scrape_page(url)

        page_title = soup.title.string
        content = soup.find_all(text=True)

        page_text_content = ''

        for t in content:
            if t.parent.name not in self.BLACKLIST:
                page_text_content += '{} '.format(t)

        return Content(page_title, page_text_content)
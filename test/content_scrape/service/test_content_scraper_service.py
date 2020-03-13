from unittest import TestCase, mock

from bs4 import BeautifulSoup

from content_scrape.service.content_scraper_service import ContentScraperService


class TestContentScraperService(TestCase):

    def mocked_scrape_page(self):
        test_file = open(__file__ + "/../../../resource/example_page_content.html", "r")
        return BeautifulSoup(test_file.read(), 'html.parser')

    @mock.patch('content_scrape.service.content_scraper_service.ContentScraperService.scrape_page',
                side_effect=mocked_scrape_page)
    def test_get_page_content(self, mock):
        content_scraper_service = ContentScraperService()
        content = content_scraper_service.get_page_content("mocked_url")

        self.assertEqual(content.title, "HTML Title", "Scraped page title!")
        self.assertEqual(content.text_content, "The content of the document...... ", "Scraped page content")

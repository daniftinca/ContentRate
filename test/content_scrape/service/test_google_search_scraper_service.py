from unittest import TestCase

from content_scrape.service.google_search_scraper_service import GoogleSearchScraperService


class TestGoogleSearchScraperService(TestCase):

    def test_get_search_result(self):
        google_search_scraper_service = GoogleSearchScraperService()
        result_list = google_search_scraper_service.get_search_result("dog")

        self.assertTrue(result_list)

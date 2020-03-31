from content_scrape.service.content_scraper_service import ContentScraperService
from content_scrape.service.google_search_scraper_service import GoogleSearchScraperService


class AnalyzerService:
    url = ''
    target_query = ''

    def __init__(self, content_url, target_query) -> None:
        super().__init__()
        self.url = content_url
        self.target_query = target_query
        self.scraping_service = ContentScraperService()
        self.google_scrape_service = GoogleSearchScraperService()

    def compare_len(self):
        request_page_content = self.scraping_service.get_page_content(self.url)
        google_content = self.google_scrape_service.get_search_result_with_content(self.target_query)

        sum = 0
        for content in google_content:
            sum += len(content.split(" "))

        target_length = sum/len(content)
        request_length = len(request_page_content.split(" "))

        return request_length,target_length

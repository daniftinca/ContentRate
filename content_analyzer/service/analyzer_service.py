from content_scrape.service.content_scraper_service import ContentScraperService
from content_scrape.service.google_search_scraper_service import GoogleSearchScraperService
import pandas as pd
import sklearn as sk
import math
from sklearn.feature_extraction.text import TfidfVectorizer

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
        request_page_content = self.scraping_service.get_page_content(self.url).text_content
        google_content = self.google_scrape_service.get_search_result_with_content(self.target_query)

        sum = 0
        for content in google_content:
            content = content.text_content
            sum += len(content.split(" "))

        target_length = sum/len(google_content)
        request_length = len(request_page_content.split(" "))

        return request_length,target_length


    def compare_tfidf_new(self):
        tfidf_vectorizer = TfidfVectorizer(use_idf=True)

        first = self.scraping_service.get_page_content(self.url)
        others = self.google_scrape_service.get_search_result_with_content(self.target_query)
        results = []
        for content in others:
            tfidf_vectorizer_vectors = tfidf_vectorizer.fit_transform([first,content])
            first_vector_tfidfvectorizer = tfidf_vectorizer_vectors[0]
            df = pd.DataFrame(first_vector_tfidfvectorizer.T.todense(), index=tfidf_vectorizer.get_feature_names(),
                              columns=["tfidf"])
            df.sort_values(by=["tfidf"], ascending=False)
            results.append(df)

        return results

    def compare_tfidf(self):
        first = self.scraping_service.get_page_content(self.url)
        others = self.google_scrape_service.get_search_result_with_content(self.target_query)
        results = []
        for content in others:
            total = set(first).union(set(content))
            wordDictA = dict.fromkeys(total, 0)
            wordDictB = dict.fromkeys(total, 0)
            for word in first:
                wordDictA[word] += 1

            for word in content:
                wordDictB[word] += 1

            pd.DataFrame([wordDictA, wordDictB])
            tfFirst = self.computeTF(wordDictA, first)
            tfSecond = self.computeTF(wordDictB, content)

            idfs = self.computeIDF([wordDictA, wordDictB])

            idfFirst = self.computeTFIDF(tfFirst, idfs)
            idfSecond = self.computeTFIDF(tfSecond, idfs)

            tfidf = pd.DataFrame([idfFirst, idfSecond])

            results.append(tfidf)

    def computeTF(self, wordDict, bow):
        tfDict = {}
        bowCount = len(bow)
        for word, count in wordDict.items():
            tfDict[word] = count / float(bowCount)
        return tfDict

    def computeIDF(self, docList):
        idfDict = {}
        N = len(docList)

        idfDict = dict.fromkeys(docList[0].keys(), 0)
        for doc in docList:
            for word, val in doc.items():
                if val > 0:
                    idfDict[word] += 1

        for word, val in idfDict.items():
            idfDict[word] = math.log10(N / float(val))

        return idfDict

    def computeTFIDF(self, tfBow, idfs):
        tfidf = {}
        for word, val in tfBow.items():
            tfidf[word] = val * idfs[word]
        return tfidf
from django.db import models


class Comparison(models.Model):
    source_article_url = models.CharField(max_length=250)
    source_article_title = models.CharField(max_length=250)
    source_article_content = models.CharField(max_length=100000)

    # mai trebuie:
    # user
    # comparison results

    def __str__(self):
        return self.source_article_url

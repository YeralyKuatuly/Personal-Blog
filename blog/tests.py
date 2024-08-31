from django.test import TestCase
from .models import Article


class ArticleModelTest(TestCase):

    def setUp(self):
        self.article = Article.objects.create(
            title="Test Article",
            content="This is a test article content.",
        )

    def test_article_creation(self):
        self.assertEqual(self.article.title, "Test Article")
        self.assertEqual(self.article.content, "This is a test article content.")

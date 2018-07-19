from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from posts.views import index
from posts.models import Post


class IndexPageTest(TestCase):

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index_page_returns_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertTrue("<title>Helpitessa's Blog", html)
        self.assertTrue(html.endswith('</html>'))

    # def test_index_page_display_all_posts(self):


class PostModelTest(TestCase):
    def test_string_representation(self):
        post = Post(title="My post title")
        self.assertEqual(str(post), post.title)

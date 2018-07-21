from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from posts.views import index
from posts.models import Post


class IndexPageTest(TestCase):

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_index(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_wrong_root(self):
        resp = self.client.get('/wrong')
        self.assertEqual(resp.status_code, 404)

    # def test_index_page_display_all_posts(self):


class PostPageTest(TestCase):
    def test_post_detail_page(self):
        posts = Post.objects.all()
        post = Post.objects.create(title='First post')
        self.assertEqual(posts[0].title, 'First post')


class PostModelTest(TestCase):
    def test_string_representation(self):
        post = Post.objects.create(title="My post title")
        self.assertEqual(str(post), post.title)
        self.assertEqual(post.id, 1)

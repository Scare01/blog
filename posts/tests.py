from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from posts.views import posts
from posts.models import Post


class IndexPageTest(TestCase):

    def test_root_url_resolves_to_index_view(self):
        found = resolve('/')
        self.assertEqual(found.func, posts)

    def test_base(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_wrong_root(self):
        resp = self.client.get('/wrong')
        self.assertEqual(resp.status_code, 404)


class PostPageTest(TestCase):
    def test_post_detail_page(self):
        Post.objects.create(title='First post')
        posts = Post.objects.all()
        self.assertEqual(posts[0].title, 'First post')


class PostModelTest(TestCase):
    def test_string_representation(self):
        post = Post.objects.create(title="My post title")
        self.assertEqual(str(post), post.title)
        self.assertEqual(post.id, 1)

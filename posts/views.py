from django.shortcuts import render, get_object_or_404
from .models import Post


def posts(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'posts/posts.html', context)


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'posts/detail.html', {'post': post})

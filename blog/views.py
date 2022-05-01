from django.shortcuts import render, redirect, get_object_or_404
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def detail(request, pk):
    post = get_object_or_404(Post, id=pk)
    context = {
        'post': post,
    }

    return render(request, 'blog/detail.html', context)

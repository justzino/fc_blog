from django.shortcuts import render

from blogs.models import Post


def posts_list(request):
    posts = Post.objects.all()

    return render(request, 'blogs/posts_list.html', context={'posts':posts})
from django.shortcuts import render

from blogs.models import Post


def posts_list(request):
    posts = Post.objects.order_by('-created_at')    # 최신순부터 게시물 정렬

    return render(request, 'blogs/posts_list.html', context={'posts':posts})
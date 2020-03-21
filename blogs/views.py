from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from blogs.models import Post


def posts_list(request):
    posts = Post.objects.order_by('-created_at')    # 최신순부터 게시물 정렬

    return render(request, 'blogs/posts_list.html', context={'posts':posts})

def post_detail(request, post_id):      
    post = get_object_or_404(Post, pk=post_id)  
    # 404 페이지 표시할 때 (첫번째 인자는 모델, 두번째 인자는 키워드 post_id가 없으면 404 에러 발생)

    return render(request, 'blogs/post_detail.html', context={'post':post})


@login_required
def post_write(request):
    errors = []
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()
        image = request.FILES.get('image')

        if not title:
            errors.append('제목을 입력해주세요.')

        if not content:
            errors.append('내용을 입력해주세요.')

        if not errors:
            post = Post.objects.create(user=request.user, title=title, content=content, image=image)

            return redirect(reverse('post_detail', kwargs={'post_id': post.id}))
    
    return render(request, 'blogs/post_write.html', {'user':request.user, 'errors':errors})
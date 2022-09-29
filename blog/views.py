from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk' #데이터 많이 들어가서 정렬 필요 밑에 상세페이지는 정렬 필요 x
    #템플릿은 모델명_list.html: post_list.html

class PostDetail(DetailView):
    model = Post
    # 템플릿은 모델명_detail.html: post_detail.html


# def index(request):
#     posts = Post.objects.all().order_by('-pk') # 정렬해 주는 명렁어 'pk'는 1 2 3으로 정렬
#     return render(request, 'blog/index.html', {'posts': posts})
#
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk) #오른쪽은 전달받은 pk
#     return render(request, 'blog/single_post_page.html', {'post': post})
#     #오른쪽에 있는 게 내가 선언해 준 거, 왼쪽은 템플릿에서 전달받는 인수 값
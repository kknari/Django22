from django.shortcuts import render
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.core.exceptions import PermissionDenied

# Create your views here.
#view에서 사용자 요구 처리

class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category', 'tags']
    template_name = 'blog/post_update_form.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user == self.get_object().author:
            return super(PostUpdate, self).dispatch(request, *args, **kwargs)
        else:
            raise PermissionDenied
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostUpdate, self).get_context_data()
        context['categories'] = Category.objects.all()  # 따옴표 안에 있는 걸 변수로, view로 전달한다
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    fields = ['title', 'hook_text', 'content', 'head_image', 'file_upload', 'category']
    # 모델명_form.html

    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_superuser or self.request.user.is_staff):
            form.instance.author = current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostCreate, self).get_context_data()
        context['categories'] = Category.objects.all()  # 따옴표 안에 있는 걸 변수로, view로 전달한다
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context


class PostList(ListView):
    model = Post
    ordering = '-pk' #데이터 많이 들어가서 정렬 필요 밑에 상세페이지는 정렬 필요 x

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all() # 따옴표 안에 있는 걸 변수로, view로 전달한다
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context
    #템플릿은 모델명_list.html: post_list.html
    #매개변수 모델명_list : post_list 라고 하는 것이 전달됨

class PostDetail(DetailView):
    model = Post
    # 템플릿은 모델명_detail.html: post_detail.html
    #매개변수 모델명 : post 라는 것을 통해 전달해 줌

    # CBV에서 추가로 넘기고 싶은 인자 있을 때 사용
    # 특정 조건 레코드만 필터링 할 때 사용
    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()  # 따옴표 안에 있는 걸 변수로, view로 전달한다
        context['no_category_post_count'] = Post.objects.filter(category=None).count() # category = None인 포스트만 필터링
        return context

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)
    return render(request, 'blog/post_list.html', {
        'category' : category,
        'post_list' : post_list,
        'categories' : Category.objects.all(),
        'no_category_post_count' : Post.objects.filter(category=None).count
    })

def tag_page(request, slug):
    tag = Tag.objects.get(slug=slug)
    post_list = tag.post_set.all()
    return render(request, 'blog/post_list.html', {
        'tag' : tag,
        'post_list' : post_list,
        'categories': Category.objects.all(),
        'no_category_post_count': Post.objects.filter(category=None).count
    })



# def index(request):
#     posts = Post.objects.all().order_by('-pk') # 정렬해 주는 명렁어 'pk'는 1 2 3으로 정렬
#     return render(request, 'blog/index.html', {'posts': posts})
#
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk) #오른쪽은 전달받은 pk
#     return render(request, 'blog/single_post_page.html', {'post': post})
#     #오른쪽에 있는 게 내가 선언해 준 거, 왼쪽은 템플릿에서 전달받는 인수 값
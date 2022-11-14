from django.urls import path
from . import views

urlpatterns = [ #IP주소/blog/
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('category/<str:slug>/', views.category_page), # IP주소/blog/category/slug/
    path('tag/<str:slug>/', views.tag_page), # IP주소/blog/tag/slug/
    path('create_post/', views.PostCreate.as_view()),
    path('update_post/<int:pk>/', views.PostUpdate.as_view()),

    # path('', views.index), #IP/blog/ 블로그 앱 밑에 있는 views로 가겠다
    # path('<int:pk>/', views.single_post_page)
]
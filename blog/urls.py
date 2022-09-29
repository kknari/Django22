from django.urls import path
from . import views

urlpatterns = [ #IP주소/blog/
    path('', views.index), #IP/blog/ 블로그 앱 밑에 있는 views로 가겠다
    path('<int:pk>/', views.single_post_page)
]
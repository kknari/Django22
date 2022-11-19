"""myPrj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [ #ip주소/
    path('admin/', admin.site.urls), #IP주소/admin/ 주소로 갔을 때 처리해 줄 수 있는 것을 보여 줌
    path('blog/', include('blog.urls')), # IP주소/blog 이런 형태의 url
    path('accounts/', include('allauth.urls')),
    path('', include('single_pages.urls')) #ip주소/
] # 사용자가 사용하는 url, 뒤에가 url 처리해 주는 값

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#스트링은 +=가 추가하는 거임 뒤에다 연결
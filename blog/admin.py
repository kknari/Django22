from django.contrib import admin
from .models import Post, Category #외부파일 불러옴

# Register your models here.

admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    # 이 필드는 어떻게 작성하겠다 미리 설정
    # slug에 있는 값을 미리 설정(카테고리의 name 입력하면 그 값 자동으로 slug에 들어감)
    # name 필드 값으로 slug 자동 생성 설정
    prepopulated_fields = {'slug' : ('name', )}

admin.site.register(Category, CategoryAdmin)
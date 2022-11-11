import os

from django.db import models
from django.contrib.auth.models import User # 다대일 관계

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return f'/blog/tag/{self.slug}/'
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/blog/category/{self.slug}/'

    # 카테고리 복수를 이렇게 정의 하겠다
    class Meta:
        verbose_name_plural = 'Categories'


class Post(models.Model): #class의 이름이 table 이름
    title = models.CharField(max_length=30) #제목
    hook_text = models.CharField(max_length=100, blank=True) #글자 수 제한 있음 / content 내용 일부 미리 보기
    content = models.TextField() #작성 내용(제한 없음)

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) # 연도/월/일 %Y=2022 %y=22로 표현
    #blank 비어 있어도 괜찮다
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True) #작성 시간
    updated_at = models.DateTimeField(auto_now=True)

    # 다대일 관계 -> 작성자
    # 마이그레이션시 1, 1 선택
    # null = True 해당 필드 값 공란이어도 o
    # on_delete => 탈퇴하면 내용 같이 사라짐 models.CASCADE /// SET_NULL 삭제되면 그냥 NULL로 설정
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    # null, blank 공란 허용
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField(Tag, blank=True) # 필드에 null은 true 이미 포함 on_delete도 이미 포함

    def __str__(self):
        return f'[{self.pk}]{self.title}:{self.author}  :  {self.created_at}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1] #a.txt -> a txt (-1은 의미적으로 가장 마지막을 가리킴)
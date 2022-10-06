from django.db import models

# Create your models here.
class Post(models.Model): #class의 이름이 table 이름
    title = models.CharField(max_length=30) #제목
    content = models.TextField() #작성 내용(제한 없음)

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True) # 연도/월/일 %Y=2022 %y=22로 표현
    #blank 비어 있어도 괜찮다
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)

    created_at = models.DateTimeField(auto_now_add=True) #작성 시간
    updated_at = models.DateTimeField(auto_now=True)
    #추후 author 작성

    def __str__(self):
        return f'[{self.pk}]{self.title}    {self.created_at}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'
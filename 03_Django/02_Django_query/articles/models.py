from django.db import models

# Create your models here.

class Article(models.Model):
    # id는 장고가 만들어준대!
    title = models.CharField(max_length=10)
    content = models.TextField() # 얘는 글자의 제한이 없엉
    # 최초 시간 기록되고 끝
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번글 - {self.title}: {self.content}'
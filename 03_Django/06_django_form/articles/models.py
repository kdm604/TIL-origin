from django.db import models
from django.conf import settings # 모델.py에서 참조할떄는 얘가 있어야댑

# Create your models here.

#hashtag
class Hashtag(models.Model):
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content


class Article(models.Model): #대문자 M 이다 뒤에 - 시험나옴
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )

    #좋아요 로직
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_articles", blank=True)

    #해쉬
    hashtags = models.ManyToManyField(Hashtag, blank=True)

    class Meta:
        ordering = ('-pk',) # 나오는 순서 반대로 나오고 튜플형태 , 꼭찍어라~

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) #related_name='comments')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pk',)

# python manage.py makemigrations
# python manage.py migrate

# python manage.py createsuperuser /// migrate 안하면 슈퍼유저 못만듬

# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     content = models.CharField(max_length=140)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         ordering=['-pk',]

#     def __str__(self):
#         return self.content





from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import Thumbnail

# 이미지 업로드 경로 커스텀
# instance => Article 모델의 인스턴스 객체
# filename => 사용자가 업로드한 파일의 이름
def articles_image_path(instance, filename):
    return f'articles/{instance.pk}번글/images/{filename}'

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    # image = models.ImageField(blank=True)
    # image_thumbnail = ImageSpecField(
    #     source='image', #원본 이미지 필드명!
    #     processors = [Thumbnail(200,300)],
    #     format = 'JPEG',
    #     options = { 'quality':90 },
    # )
    image = ProcessedImageField(
        processors=[Thumbnail(200, 300)], # 처리할 이미지 사이즈
        format='JPEG', # 처리할 이미지 확장자(포맷)
        options={'quality':90}, # 추가 옵션 (원본의 90% 압축)
        upload_to = articles_image_path, #'articles/images', # MEDIA_ROOR(media)/articles/images 
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Create your models here.

    def __str__(self):
        return f'제목: {self.title}, 내용: {self.content}'


class Comment(models.Model): # 게시글을 삭제하면 그와 관련댄 댓글들 다삭제하는 on_delete=models.CASCADE
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    content = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk',]

    def __str__(self):
        # return f'댓글: {self.content}'
        return f'<Article({self.article_id}) : Comment({self.pk} - {self.content})>'



class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-pk',]

    def __str__(self):
        return self.content
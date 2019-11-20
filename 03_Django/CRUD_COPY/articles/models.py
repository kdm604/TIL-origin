from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
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
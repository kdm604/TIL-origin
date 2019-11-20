from django.contrib import admin
from .models import Article, Comment, Hashtag  # 모델에서 아티클 가져와야지 ㅋ

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'content', 'created_at', 'updated_at',)


# admin.site.register(Article, ArticleAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk','content', 'created_at', 'updated_at',)

# admin.site.register(Comment, CommentAdmin)


class HashtagAdmin(admin.ModelAdmin):
    list_display = ('content',)
admin.site.register(Hashtag, HashtagAdmin)

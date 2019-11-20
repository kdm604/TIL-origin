### 중요한 forms.py ####
from django import forms
from .models import Article, Comment

# 모델 뽀오오오오오옹옴
class ArticleForm(forms.ModelForm):
    # 메타정보 정보에의한 정보 ?__? 

    title = forms.CharField(
        max_length=10,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'my-title',
                'placeholder': 'Enter the Title',
            }
        )
    )

    content = forms.CharField(
        label="내용",
        widget=forms.Textarea(
            attrs={
                'class': 'my-content',
                'placeholder': 'Enter the Content',
                'rows':5,
                'cols':50,
            }
        )
    )

    class Meta:
        model = Article
        # fields = '__all__'
        fields = ('title','content',)
        # widgets = {
        #     'title': forms.TextInput(
        #         attrs={
        #             'class': 'my-title',
        #             'placeholder': 'Enter the title!',
        #         }
        #     )
        # }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


# class ArticleForm(forms.Form):
#     # title = forms.CharField(max_length=20)
#     # content = forms.CharField(widget=forms.Textarea)

#     title = forms.CharField(
#         max_length=20,
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'my-title',
#                 'placeholder' : 'Enter the title!',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'my-content',
#                 'placeholder' : 'Enter the Content!',
#                 'rows':5,
#                 'cols':50,
#             }
#         )
#     )


# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         fields = ('content',)


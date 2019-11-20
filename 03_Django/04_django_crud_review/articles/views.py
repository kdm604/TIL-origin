from django.shortcuts import render, redirect
from .models import Article, Comment
from django.core.exceptions import ValidationError
from IPython import embed

def index(request):
    # articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-pk')
    # print(articles)
    # print(type(articles))
    context = {
        'articles': articles
    }
    return render(request, 'articles/index.html',context)

# def new(request):
#     # embed()
#     return render(request, 'articles/new.html')

def create(request):
    # try:
    #     title = request.POST.get('title')
    #     content = request.POST.get('content')
    #     article = Article(title=title, content=content)
    #     article.full_clean()
    # except ValidationError:
    #     raise ValidationError('Your Error Messasge')
    # else:
    #     article.save()
    #     # return redirect(f'/articles/{article.pk}/')
    #     return redirect('articles:detail', article.pk)

    # POST 요청일때
    if request.method == 'POST': 
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        article = Article(title=title, content=content, image=image)
        article.save()
        # embed()

#     # #1. 
#     # article = Article()
#     # article.title = title
#     # article.content = content
#     # article.save()

#     #2
    

#     #3 
#     # Article.objects.create(title=title, content=content)

#     # return render(request, 'articles/index.html')
#     # return redirect('/articles/')
        return redirect(f'/articles/{article.pk}/')
    # GET 요청일때
    else:
        return render(request, 'articles/create.html')

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comments = article.comments.all()
    context = {'article': article, 'comments':comments,}


    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'POST':
        # num = request.POST.get('pk')
        article.delete()

        return redirect('articles:index')
    else:
        return redirect('articles:index')

# def edit(request, pk):
#     article = Article.objects.get(pk=pk)
#     context = {'article': article}

#     return render(request, 'articles/edit.html', context)


def update(request, article_pk):
    # embed()

    article = Article.objects.get(pk=article_pk)
    if request.method =='POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        # article = Article.objects.get(pk=pk)
        article.title = title #request.POST.get('title')
        article.content = content #request.POST.get('content')
        article.image = image
        
        article.save()
        return redirect('articles:detail', article.pk)
    else:
        # article = Article.objects.get(pk=pk)
        context = {'article': article}

        return render(request, 'articles/update.html', context)

def comments_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)

    if request.method == 'POST':
        content = request.POST.get('content')
        comment = Comment(article=article, content=content)
        comment.save()
        return redirect('articles:detail', article.pk)
    else:
        return redirect('articles:detail',article.pk)

def comments_delete(request, article_pk, comment_pk):
    if request.method=='POST':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
        # return redirect('article:detail', article_pk)
    return redirect('articles:detail', article_pk)


def comments_update(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.method == 'POST':
        comment.content = request.POST.get('content')
        comment.save()
        return redirect('articles:detail', article_pk)
    else:
        context = {'comment': comment}
        return render(request, 'articles/comments_update.html', context)

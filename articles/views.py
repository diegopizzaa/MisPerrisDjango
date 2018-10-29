from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms


def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})


def article_detail(request, slug):
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            # save article to db
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})


def article_edit(request, slug):
    article = get_object_or_404(Article, slug=slug)
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('article_detail', slug=article.slug)
    else:
        form = forms.CreateArticle(instance=article)
    return render(request, 'articles/article_edit.html', {'form': form})

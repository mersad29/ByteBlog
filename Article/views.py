from django.shortcuts import render, get_object_or_404
from .models import Article


def ArticleDetailView(request, slug):
    articles = Article.objects.get(slug=slug)

    context = {
        'articles': articles
    }

    return render(request, 'Article/ArticleDetail.html', context)


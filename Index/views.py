import datetime
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import View, TemplateView, ListView
from Article.models import Article, Category, Like, Comment
from . import models
from persiantools.jdatetime import JalaliDate


def index(request):
    articles = Article.objects.all().order_by('-created_time')
    categories = Category.objects.all().order_by('-created_time')
    advertisement = models.LeftNavbar.objects.all().first()
    article_count = Article.objects.count()

    for cat in categories:
        cat.prev = categories.filter(created_time__lt=cat.created_time).first()
        if not cat.prev:
            cat.color = 'nav-elipse-red'
        else:
            if cat.prev.color == 'nav-elipse-red':
                cat.color = 'nav-elipse-blue'
            elif cat.prev.color == 'nav-elipse-blue':
                cat.color = 'nav-elipse-green'
            elif cat.prev.color == 'nav-elipse-green':
                cat.color = 'nav-elipse-yellow'
            else:
                cat.color = 'nav-elipse-red'

    for article in articles:
        article.prev = articles.filter(created_time__lt=article.created_time).first()
        if not article.prev:
            article.color = 'red-article'
        else:
            if article.prev.color == 'red-article':
                article.color = 'blue-article'
            elif article.prev.color == 'blue-article':
                article.color = 'green-article'
            elif article.prev.color == 'green-article':
                article.color = 'yellow-article'
            else:
                article.color = 'red-article'

        article.c = article.comments.filter(published=True).count()

    Article.objects.bulk_update(articles, ['color'])
    Category.objects.bulk_update(categories, ['color'])
    paginator = Paginator(articles, 4)
    page_number = request.GET.get('page')
    objects_list = paginator.get_page(page_number)

    for article in articles:
        created_time = article.created_time
        article.jalali = JalaliDate(datetime.date
                                    (created_time.year, created_time.month, created_time.day)).strftime('%c', 'fa')
        time_difference = timezone.now() - article.created_time
        article.time_difference = time_difference.total_seconds() // 3600

    context = {
        'articles': objects_list,
        'art': articles,
        'categories': categories,
        'article_count': article_count,
        'ad': advertisement,
    }
    return render(request, 'index.html', context)


def like(request, slug, pk):
    try:
        like = Like.objects.get(article__slug=slug)
        like.delete()
    except:
        Like.objects.create(article_id=pk)
    return redirect('index:index')


def article_list(request, pk):
    category = Category.objects.get(pk=pk)
    articles = Article.objects.filter(category=category)

    context = {
        'category': category,
        'articles': articles
    }
    return render(request, 'article_list.html', context)


def about_me(request):
    return render(request, 'about-me.html')


def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        body = request.POST.get('body')
        created_at = request.POST.get('created_at')
        models.Inbox.objects.create(name=name, email=email, body=body, created_at=created_at)

    return render(request, 'contact_us.html')


def search(request):
    q = request.GET.get('q')
    articles = Article.objects.filter(title__icontains=q)

    return render(request, 'article_list.html', {'articles': articles})

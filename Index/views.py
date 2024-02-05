from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.views.generic import View, TemplateView
from Article.models import Article, Category, Like


def index(request):
    articles = Article.objects.all().order_by('-created_time')
    categories = Category.objects.all()

    paginator = Paginator(articles, 2)
    page_number = request.GET.get('page')
    objects_list = paginator.get_page(page_number)

    for article in articles:
        time_difference = timezone.now() - article.created_time
        article.time_difference = time_difference.total_seconds() // 3600

    context = {
        'articles': objects_list,
        'categories': categories,
        'like': like,
    }
    return render(request, 'index.html', context)

def like(request, slug, pk):
    try:
        like = Like.objects.get(article__slug=slug)
        like.delete()
    except:
        Like.objects.create(article_id=pk)
    return redirect('index:index')

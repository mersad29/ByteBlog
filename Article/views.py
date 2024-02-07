from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Like, Comment


def ArticleDetailView(request, slug):
    articles = get_object_or_404(Article, slug=slug)
    like = Like.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        body = request.POST.get('body')
        parent = request.POST.get('parent')
        Comment.objects.create(article=articles, name=name, body=body, parent_id=parent)

    if like.filter(article__slug=articles.slug, article_id=articles.id):
        liked = True
    else:
        liked = False

    context = {
        'articles': articles,
        'like': like,
        'liked': liked
    }

    return render(request, 'Article/ArticleDetail.html', context)

def like(request, slug, pk):
    try:
        like = Like.objects.get(article__slug=slug)
        like.delete()
    except:
        Like.objects.create(article_id=pk)
    return redirect('Articles:article_detail', slug)

from django.shortcuts import redirect, get_object_or_404, render
from django.views.generic import DetailView
from .models import Article, Like, Comment


# class ArticleDetailView(DetailView):
#     model = Article
#     template_name = 'Article/ArticleDetail.html'
#     context_object_name = 'articles'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['like'] = Like.objects.all().filter(article__slug=self.object.slug, article_id=self.object.id)
#         context['liked'] = context['like'].filter(article__slug=self.object.slug, article_id=self.object.id)
#
#         # articles = self.get_object()
#         # context['comments'] = Comment.objects.filter(article=articles, published=True)
#
#         return context
#
#     def post(self, request, *args, **kwargs):
#         name = request.POST.get('name')
#         body = request.POST.get('body')
#         parent = request.POST.get('parent')
#         articles = self.get_object()
#         Comment.objects.create(article=articles, name=name, body=body, parent_id=parent)
#
#         context = self.get_context_data()
#         return self.render_to_response(context)

def ArticleDetailView(request, slug):
    articles = get_object_or_404(Article, slug=slug)
    like = Like.objects.all().filter(article__slug=articles.slug, article_id=articles.id)
    next_article = Article.objects.filter(created_time__gt=articles.created_time).order_by('created_time').first()
    prev_article = Article.objects.filter(created_time__lt=articles.created_time).order_by('-created_time').first()
    comments = Comment.objects.filter(article=articles, published=True).count()

    if request.method == 'POST':
        name = request.POST.get('name')
        body = request.POST.get('body')
        parent = request.POST.get('parent')
        email = request.POST.get('email')
        Comment.objects.create(article=articles, name=name, body=body, parent_id=parent, email=email)

    if like.filter(article__slug=articles.slug, article_id=articles.id):
        liked = True
    else:
        liked = False


    context = {
        'articles': articles,
        'like': like,
        'liked': liked,
        'comments': comments,
        'next_article': next_article,
        'prev_article': prev_article,
    }

    return render(request, 'Article/ArticleDetail.html', context)


def like(request, slug, pk):
    try:
        like = Like.objects.get(article__slug=slug)
        like.delete()
    except:
        Like.objects.create(article_id=pk)

    return redirect('Articles:article_detail', slug)

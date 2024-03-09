from django.shortcuts import render, get_object_or_404
from Account import models
from Account.models import CustomUser
from Article import models
from Article.models import Comment
from Index.models import HeaderBasement, FooterBasement

def all_categories(request):
    category = models.Category.objects.all()
    return {'all_categories': category}

def article_count(request):
    article_count = models.Article.objects.count()
    return {'article_count': article_count}

def all_articles(request):
    all_articles = models.Article.objects.all().order_by('-created_time')
    return {'all_articles': all_articles}

def header(request):
    header_title = HeaderBasement.objects.all()
    return {'header_title': header_title}

def footer(request):
    footer_description = FooterBasement.objects.all()
    return {'footer_description': footer_description}

def admin_user(request):
    users = CustomUser.objects.all()
    return {'admin_user': users}

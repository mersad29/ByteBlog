from django.urls import path
from . import views
from .views import ArticleDetailView

app_name = 'Articles'
urlpatterns = [
    path('detail/<slug:slug>', views.ArticleDetailView, name='article_detail'),
    path('like/<slug:slug>/<int:pk>', views.like, name='like'),
]
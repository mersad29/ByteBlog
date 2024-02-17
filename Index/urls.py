from django.urls import path
from . import views
app_name = 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('like/<slug:slug>/<int:pk>', views.like, name='like'),
    path('articles/list/<int:pk>', views.article_list, name='article_list'),
    path('about_me', views.about_me, name='about_me'),
    path('contact_us', views.contact_us, name='contact_us'),
    path('search/', views.search, name='search'),
]
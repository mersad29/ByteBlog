from django.urls import path
from . import views
app_name = 'index'
urlpatterns = [
    path('', views.index, name='index'),
    path('like/<slug:slug>/<int:pk>', views.like, name='like'),
]
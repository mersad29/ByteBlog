from django.contrib import admin
from . import models

@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_time')

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
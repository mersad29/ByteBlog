from django.contrib import admin
from .models import HeaderBasement, FooterBasement, Inbox

admin.site.register(HeaderBasement)
admin.site.register(FooterBasement)
admin.site.register(Inbox)
from django.contrib import admin
from .models import Article, BlogComment, Category, Tag

# Register your models here.
admin.site.register([Article, Category, BlogComment, Tag])
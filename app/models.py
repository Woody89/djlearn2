from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Article(models.Model):
    
    STATUS_CHOICES = (
                      ('d', 'part'),
                      ('p', 'published'),
                      )
    
    title = models.CharField('Title', max_length=100)
    body = models.TextField('Body')
    created_time = models.DateTimeField('Created_time', auto_now_add=True)
    last_modified_time = models.DateTimeField('Last_update_time',
                                              auto_now=True)
    status = models.CharField('Status', max_length=1, choices=STATUS_CHOICES)
    abstract = models.CharField('Abstract', max_length=50, blank=True,
                                null=True, help_text='Optional')
    views = models.PositiveIntegerField('Views', default=0)
    likes = models.PositiveIntegerField('Likes', default=0)
    topped = models.BooleanField('Topped', default=False)
    category = models.ForeignKey('Category', verbose_name='Category',
                                 null=True, on_delete=models.SET_NULL)
    tags = models.ManyToManyField('Tag', verbose_name='Tag cloud',
                                  blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-last_modified_time']
    
    def get_absolute_url(self):
        return reverse('app:detail', kwargs={'article_id': self.pk})


class Category(models.Model):
    
    name = models.CharField('Category_name', max_length=20)
    created_time = models.DateTimeField('Created_time', auto_now_add=True)
    last_modified_time = models.DateTimeField('Last_update_time',
                                              auto_now=True)
    
    def __str__(self):
        return self.name
    

class Tag(models.Model):
    
    name = models.CharField('Tag_name', max_length=20)
    created_time = models.DateTimeField('Created_time', auto_now_add=True)
    last_modified_time = models.DateTimeField('Last_update_time',
                                              auto_now=True)
    
    def __str__(self):
        return self.name


class BlogComment(models.Model):
    
    user_name = models.CharField('commentor_name', max_length=100)
    body = models.TextField('connemt_context')
    created_time = models.DateTimeField('comment_time', auto_now_add=True)
    article = models.ForeignKey('Article', verbose_name='commented_article', on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:20]


class Suggest(models.Model):
    
    suggest = models.TextField('suggestion', max_length=200)
    suggest_time = models.DateTimeField('suggest_time', auto_now_add=True)

    def __str__(self):
        return self.suggest


class Imitate(models.Model):
    
    imitate_name = models.TextField('imitate_name', max_length=20)
    imitate_time = models.DateTimeField('imitate_time', auto_now_add=True)
    
    def __str__(self):
        return self.imitate_name
    
class User(models.Model):
    username = models.CharField('username', max_length=20)
    password = models.CharField('password', max_length=20)
    email = models.EmailField()
    
    def __str__(self):
        return models.Model.__str__(self)
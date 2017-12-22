from django.conf.urls import url
from . import views
from django.views.decorators.cache import cache_page

app_name = 'app'
urlpatterns = [
               url(r'^$', views.IndexView.as_view(), name='index'),
               url(r'^article/(?P<article_id>\d+)$', 
                   cache_page(60*15)(views.ArticleDetailView.as_view()), name='detail'),
               url(r'^search/$', views.blog_search, name='search'),
               url(r'^about_me/$', views.suggest_view, name='about_me'),
               url(r'^imitate/$', views.imitate_view, name='imitate'),
               url(r"^category/(?P<cate_id>\d+)$", views.CategoryView.as_view(), name='category'),
               url(r'^article/(?P<article_id>\d+)/comment/$', views.CommentView, name='comment'),
               url(r'^tags/(?P<tag_id>\d+)$', views.TagView.as_view(), name='tag'),
               url(r'^thanks/$', views.thanks, name='thanks'),
               url(r'^success/$', views.success, name='success'),
               url(r'^regist/$', views.regist, name='regist'),
               url(r'^login/$', views.login, name='login'),
               ]
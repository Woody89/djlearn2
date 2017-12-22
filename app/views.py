import markdown
import re
import logging

from django.shortcuts import render, get_object_or_404, get_list_or_404,\
    redirect
from django.views.generic.list import ListView
from app.models import Article, Category, Tag, Suggest, BlogComment, Imitate, User
from django.views.generic.detail import DetailView
from .forms import BlogCommentForm, SuggestForm, ImitateForm, UserForm

logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(ListView):
    
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    
    def get_queryset(self):
        article_list = Article.objects.filter(status='p')
        for article in article_list:
            article.body = markdown.markdown(article.body,)
        return article_list
    
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(IndexView, self).get_context_data(**kwargs)


class ArticleDetailView(DetailView):
    
    model = Article
    template_name = 'blog/detail.html'
    context_object_name = 'article'
    pk_url_kwarg = 'article_id'
    
    def get_object(self, queryset=None):
        obj = super(ArticleDetailView, self).get_object()
        obj.views += 1
        obj.save()
        obj.body = markdown.markdown(obj.body, safe_mode='escape',
                                     extentions=[
                                                 'markdown.extentions.nl2br',
                                                 'markdown.extentions.fenced_code',
                                                 ]
                                     )
        return obj
    
    def get_context_data(self, **kwargs):
        kwargs['comment_list'] = self.object.blogcomment_set.all()
        kwargs['form'] = BlogCommentForm()
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        return super(ArticleDetailView, self).get_context_data(**kwargs)


class CategoryView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'
    
    def get_queryset(self):
        article_list = Article.objects.filter(category=self.kwargs['cate_id'], status='p')
        for article in article_list:
            article.body = markdown.markdown(article.body)
        return article
    
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('name')
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        name = get_object_or_404(Category, pk=self.kwargs['cate_id'])
        kwargs['cate_name'] = name
        return super(CategoryView, self).get_context_data(**kwargs)


class TagView(ListView):
    template_name = 'blog/index.html'
    context_object_name = 'article_list'

    def get_queryset(self):
        article_list = Article.objects.filter(tags=self.kwargs['tag_id'], status='p')
        for article in article_list:
            article.body = markdown.markdown(article.body, extras=['fenced-code-blocks'], )
        return article_list

    def get_context_data(self, **kwargs):
        kwargs['tag_list'] = Tag.objects.all().order_by('name')
        kwargs['category_list'] = Category.objects.all().order_by('name')
        name = get_object_or_404(Tag, pk=self.kwargs['tag_id'])
        kwargs['tag_name'] = name
        return super(TagView, self).get_context_data(**kwargs)
    
    
def CommentView(request, article_id):
    if request.method == 'POST':
        form = BlogCommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['user_name']
            body = form.cleaned_data['body']
            logger.info("name: %s", name)

            article = get_object_or_404(Article, pk=article_id)
            new_record = BlogComment(user_name=name,
                                 body=body,
                                article=article)
            new_record.save()
            return redirect('app:detail', article_id=article_id)


def blog_search(request,):
    search_for = request.GET['search_for']
    if search_for:
        results = []
        article_list = get_list_or_404(Article)
        category_list = get_list_or_404(Category)
        for article in article_list:
            if re.findall(search_for, article.title):
                results.append(article)
        for article in results:
            article.body = markdown.markdown(article.body,)
        tag_list = Tag.objects.all().order_by('name')
        return render(request, 'blog/search.html', {
                        'article_list': results,
                        'category_list': category_list,
                        'tag_list': tag_list,
                        })
    else:
        return redirect('app/index')

def suggest_view(request):
    form = SuggestForm()
    if request.method == 'POST':
        form = SuggestForm(request.POST)
        if form.is_valid():
            suggest_data = form.cleaned_data['suggest']
            new_record = Suggest(suggest=suggest_data)
            new_record.save()
            return redirect('app:thanks')
    return render(request, 'blog/about.html', {'form': form})

#user regist 
def regist(request):
    userform = UserForm()
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            email = userform.cleaned_data['email']
            user = User.objects.create(username=username, password=password, email=email)
            User.save(user)
            return redirect('app:success')
    return render(request, 'blog/regist.html', {'userform': userform})

def login(request):
    userform = UserForm
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            username = userform.cleaned_data['username']
            password = userform.cleaned_data['password']
            user = User.objects.filter(username=username,
                                       password=password)
            if user:
                request.session['username'] = username
                return redirect('app:index')
    return render(request, 'blog/login.html', {'userform': userform})

def imitate_view(request):
    form = ImitateForm()
    if request.method == 'POST':
        form = ImitateForm(request.POST)
        if form.is_valid():
            imitate_data = form.cleaned_data['imitate_name']
            new_record = Imitate(imitate_name=imitate_data)
            new_record.save()
            return redirect('app:thanks')
    return render(request, 'blog/about.html', {'form': form})

def thanks(request,):
    return render(request, 'blog/thanks.html')

def success(request):
    return render(request, 'blog/success.html')
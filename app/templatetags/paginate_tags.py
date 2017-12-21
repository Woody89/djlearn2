from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

register = template.Library()

@register.simple_tag(takes_context=True)
def paginate(context, object_list, page_count):
    
    paginator = Paginator(object_list, page_count)
    page = context['request'].GET.get('page')
    
    try:
        object_list = paginator.page(page)
        context['current_page'] = int(page)
        pages = paginator.page_range
    except PageNotAnInteger:
        object_list = paginator.page(1)
        context['current_page'] = 1
        pages = paginator.page_range
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
        context['current_page'] = paginator.num_pages
        pages = paginator.page_range
    
    context['article_list'] = object_list
    context['pages'] = pages
    context['last_page'] = paginator.num_pages
    context['first_page'] = 1
    
    try:
        context['page_first'] = pages[0]
        context['page_last'] = pages[-1] + 1
    except IndexError:
        context['page_first'] = 1
        context['page_last'] = 2
    
    return ''
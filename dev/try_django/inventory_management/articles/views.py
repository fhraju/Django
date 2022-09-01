from multiprocessing import context
from django.shortcuts import render

from .models import Article

# Create your views here.
def article_search_view(request):
    context = {}
    return render(request, "articles/search.html", context=context)

def article_create_view(request, id=None):
    context = {}
    if request.method == 'POST':
        title = request.POST.get("title")
        content = request.POST.get("content")
        print(title, content)
        article_object = Article.objects.create(title=title, content=content)
        context['object'] = article_object
        context['created'] = True
    return render(request,"articles/create.html",context=context)

def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id=id)
    context = {
        "object": None,
    }
    return render(request,"articles/detail.html",context={})
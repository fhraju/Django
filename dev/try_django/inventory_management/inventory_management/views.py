"""
To render html web pages
"""
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from articles.models import Article


def home_view(request):
    """
    Take in a request (Django sends the request)
    Return HTML as a Response (We pick to return the response)
    """
    random_id = random.randint(1,3)
    #From the database
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()

    context = {"object_list": article_queryset,
    'title': article_obj.title,
    "id": article_obj.id,
    'content': article_obj.content}

    #Django Template demo
    HTML_STRING = render_to_string("C:/Users/along/OneDrive/Documents/GitHub/Django/dev/try_django/inventory_management/templates/home_view.html", context=context)
    # HTML_STRING = """
    # <h1>{title} ({id})</h1>
    # <p>Hi, {content}!</p>
    # """.format(**context)

    return HttpResponse(HTML_STRING)
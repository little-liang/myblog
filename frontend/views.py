from django.shortcuts import render
from backend.models import *
import datetime
# Create your views here.


def index(request):
    article_info = Article.objects.all().order_by('publish_time')
    for article in article_info:
        article.publish_time = datetime.datetime.strftime(article.publish_time, "%Y-%m-%d")
    return render(request, 'frontend/index.html', context={'article_info': article_info})


def article(request):
    return render(request, 'frontend/article.html')

def category(request):
    return render(request, 'frontend/category.html')

def error(request):
    return render(request, 'frontend/404.html')

def readers(request):
    return render(request, 'frontend/readers.html')

def tags(request):
    return render(request, 'frontend/tags.html')

def links(request):
    return render(request, 'frontend/links.html')

def UpgradeBrowser(request):
    return render(request, 'frontend/UpgradeBrowser.html')
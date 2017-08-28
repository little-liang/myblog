from django.shortcuts import render

# Create your views here.
from Blog.models import Article
import markdown
def index(request):

    return render(request, 'index.html')

def article_admin(request):


    article_list = Article.objects.all()

    return render(request, 'article_admin.html', context={'article_list': article_list})


def edit_article(request):
    article_list = Article.objects.all()

    return render(request, 'edit_article.html', context={'article_list': article_list})

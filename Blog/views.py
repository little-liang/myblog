from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from Blog.models import Article
def index(request):

    return render(request, 'index.html')

def article_admin(request):

    article_list = Article.objects.all()

    return render(request, 'article_admin.html', context={'article_list': article_list})


def edit_article(request):
    article_list = Article.objects.all()

    return render(request, 'edit_article.html', context={'article_list': article_list})

@csrf_exempt
def submit_article_id(request):
    print(request.POST)
    return render(request, 'edit_article.html', context={'article_list': 'ddd'})
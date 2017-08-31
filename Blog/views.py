from django.shortcuts import render, HttpResponseRedirect
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from Blog.models import Article
def index(request):

    return render(request, 'index.html')

def article_admin(request):
    article_list = Article.objects.all()
    return render(request, 'article_admin.html', context={'article_list': article_list})


def edit_article(request):
    print(request.GET)
    print(json.dumps(request.GET))
    aa = request.GET.get('article-id')
    print(aa)


    article_id_info = Article.objects.filter(id=int(aa))
    print(article_id_info[0].id)
    return render(request, 'edit_article.html', context={'article_list': 'll'})

@csrf_exempt
def submit_article_id(request):
    print(request.POST)
    article_id = request.POST
    return render(request, 'edit_article.html', context={'article_list': article_id})
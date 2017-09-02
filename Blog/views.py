from django.shortcuts import render, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from Blog.models import Article
def index(request):

    return render(request, 'index.html')

def article_admin(request):
    article_list = Article.objects.all()
    return render(request, 'article_admin.html', context={'article_list': article_list})

@csrf_exempt
def edit_article(request):
    if request.GET:
        print(request.GET.get('article-id'))
        artitle_id = request.GET.get('article-id')
        article_info = Article.objects.filter(id=int(artitle_id))[0]
        return render(request, 'edit_article.html', context={'article_info': article_info})
    elif request.POST:
        print(request.POST)

        update_id = request.POST.get('id')
        update_title = request.POST.get('title_post')
        update_content = request.POST.get('content_post')

        update_sql_obj = Article.objects.get(id=int(update_id))

        update_sql_obj.title = update_title
        update_sql_obj.content = update_content

        update_sql_obj.save()

        print(update_sql_obj)

        return render(request, 'article_admin.html')
    else:
        return render(request, 'edit_article.html')

@csrf_exempt
def submit_article_id(request):
    print(request.POST)
    # article_id = request.POST
    # return render(request, 'edit_article.html', context={'article_list': article_id})
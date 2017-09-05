from django.shortcuts import render, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from Blog.models import *
def index(request):

    return render(request, 'index.html')

def article_admin(request):
    article_list = Article.objects.all()
    return render(request, 'article_admin.html', context={'article_list': article_list})

@csrf_exempt
def edit_article(request):
    if request.GET:
        # print(request.GET)
        # print(request.GET.get('command'))
        # print(request.GET.get('article-id'))

        #跳转展示文章
        if request.GET.get('command') == 'null':
            print(request.GET.get('article-id'))
            artitle_id = request.GET.get('article-id')
            article_info = Article.objects.filter(id=int(artitle_id))[0]
            return render(request, 'edit_article.html', context={'article_info': article_info})

        #删除文章
        if request.GET.get('command') == 'delete':
            print(request.GET.get('article-id'))
            artitle_id = request.GET.get('article-id')
            delete_sql_obj = Article.objects.get(id=int(artitle_id))
            delete_sql_obj.delete()
            return HttpResponse("delete ok")

    elif request.POST:
        print(request.POST)
        if request.POST.get('id'):
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

            print(request.POST)
            content = request.POST.get('content_post')
            title = request.POST.get('title_post')
            author = 'me'
            canbe_content = True

            ##
            tags = 'linux'
            ##
            catagory = '社会'

            tags_obj = Tag.objects.get(name='linux')
            catagory_obj = Catagory.objects.get(name='linux')


            create_sql_obj = Article.objects.create(
                catagory=catagory_obj,
                title=title,
                content=content,
                author=author,
                canbe_content=canbe_content,
            )

            create_sql_obj.save()

            #只有多对多关系才需要有记录后,才能添加
            create_sql_obj.tags.add(tags_obj)
            create_sql_obj.save()

            print('adsggadsfasdgdsgsddsfg')
            return render(request, 'article_admin.html')

    else:
        return render(request, 'edit_article.html')

@csrf_exempt
def submit_article_id(request):
    print(request.POST)
    # article_id = request.POST
    # return render(request, 'edit_article.html', context={'article_list': article_id})
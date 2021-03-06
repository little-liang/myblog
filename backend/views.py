
from django.shortcuts import render, HttpResponse, redirect
import json, datetime
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
# coding:utf-8
# Create your views here.
from backend.models import *

@csrf_exempt
def article_admin(request):
    if request.POST:
        #全部删除
        if request.POST.getlist('select_checked_article_list[]'):
            for line in request.POST.getlist('select_checked_article_list[]'):
                delete_sql_obj = Article.objects.get(id=int(line))
                delete_sql_obj.delete()

            return HttpResponse("delete all OK")
    else:
        every_page_num = 4  # 每页显示的记录数  #不加 order by 会有警告信息
        p = Paginator(Article.objects.all().order_by('-publish_time',), every_page_num)

        ##前端点击的page,第几页
        page = request.GET.get('page')


        print(type(page))
        #当前页第一个文章的编号
        if page == None:
            page = 1
        current_page_first = (int(page) - 1) * every_page_num

        try:
            contacts = p.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            contacts = p.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            contacts = p.page(p.num_pages)


        for line in contacts:
            line.publish_time = datetime.datetime.strftime(line.publish_time, "%Y-%m-%d")


        return render(request, 'backend/article_admin.html', context={
            'contacts': contacts, 'every_page_num': every_page_num,
            'current_page_first': current_page_first,
        })



@csrf_exempt
def edit_article(request):
    if request.GET:
        # print(request.GET)
        # print(request.GET.get('command'))
        # print(request.GET.get('article-id'))

        #跳转展示文章
        if request.GET.get('command') == 'null':
            artitle_id = request.GET.get('article-id')
            article_info = Article.objects.filter(id=int(artitle_id))[0]

            current_catagory_info = article_info.catagory.name


            all_catagory_info = Catagory.objects.all()

            all_catagory_info_list = [line.name for line in all_catagory_info]


            return render(
                request, 'backend/edit_article.html', context={
                    'article_info': article_info, 'current_catagory_info': current_catagory_info,
                    'all_catagory_info_list': all_catagory_info_list,
                }
            )

        #删除文章
        if request.GET.get('command') == 'delete':
            artitle_id = request.GET.get('article-id')
            delete_sql_obj = Article.objects.get(id=int(artitle_id))
            delete_sql_obj.delete()
            return HttpResponse("delete ok")


    ##修改文章
    elif request.POST:
        if request.POST.get('id'):
            update_id = request.POST.get('id')
            update_title = request.POST.get('title_post')
            update_content = request.POST.get('content_post')
            update_summary = request.POST.get('summary_post')


            update_sql_obj = Article.objects.get(id=int(update_id))


            update_sql_obj.title = update_title
            update_sql_obj.content = update_content
            update_sql_obj.summary = update_summary
            update_sql_obj.viwes_num = 1

            catagory_obj = Catagory.objects.get(name=request.POST.get('catagory_post'))

            update_sql_obj.catagory = catagory_obj

            update_sql_obj.save()

            ##后台传给前台数据 只有这样 ajax 才认为自己成功了
            # ret = {'status': True, 'error': ""}
            # j_ret = json.dumps(ret)
            # return HttpResponse(j_ret)

            ##这样也行
            name_dict = {'twz': 'Love python and Django', 'zqxt': 'I am teaching Django'}
            return JsonResponse(name_dict)

        else:
            ###添加新文章/`
            content = request.POST.get('content_post')
            title = request.POST.get('title_post')
            summary = request.POST.get('summary_post')
            author = 'me'
            canbe_content = True

            print(request.POST.get('catagory_post'))
            catagory_obj = Catagory.objects.get(name=request.POST.get('catagory_post'))
            create_sql_obj = Article.objects.create(
                catagory=catagory_obj,
                title=title,
                content=content,
                author=author,
                canbe_content=canbe_content,
                summary=summary,
                viwes_num=1,
            )

            create_sql_obj.save()

            #只有多对多关系才需要有记录后,才能添加
            ##
            tags = 'linux'

            tags_obj = Tag.objects.get(name='linux')
            create_sql_obj.tags.add(tags_obj)
            create_sql_obj.save()

            return HttpResponse('ok')

    else:
        all_catagory_info = Catagory.objects.all()
        all_catagory_info_list = [line.name for line in all_catagory_info]
        return render(request, 'backend/edit_article.html', context={'all_catagory_info_list': all_catagory_info_list})

@csrf_exempt
def submit_article_id(request):
    print(request.POST)
    # article_id = request.POST
    # return render(request, 'edit_article.html', context={'article_list': article_id})


@csrf_exempt
def tags_admin(request):

    if request.POST:
        print(request.POST)
        tag_id = request.POST.get('key_post')
        tag_name = request.POST.get('value_post')

        print(tag_id, tag_name)

        update_obj = Tag.objects.get(id=int(tag_id))
        update_obj.name = tag_name
        update_obj.save()


        return render(request, 'backend/tags_admin.html')
    else:
        tags_info = Tag.objects.all()
        every_page_num = 4  # 每页显示的记录数  #不加 order by 会有警告信息
        p = Paginator(Tag.objects.all().order_by('-id', ), every_page_num)


        ##前端点击的page,第几页
        page = request.GET.get('page')


        # 当前页第一个文章的编号
        if page == None:
            page = 1
        current_page_first = (int(page) - 1) * every_page_num

        try:
            page_obj = p.page(page)

        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            page_obj = p.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            page_obj = p.page(p.num_pages)

        return render(request, 'backend/tags_admin.html', context={'tags_info': tags_info, 'page_obj': page_obj, 'current_page_first': current_page_first})


@csrf_exempt
def catagory_admin(request):
    if request.POST:
        print(request.POST)
        catagory_id = request.POST.get('key_post')
        catagory_name = request.POST.get('value_post')

        update_obj = Catagory.objects.get(id=int(catagory_id))
        update_obj.name = catagory_name
        update_obj.save()

        ajax_success_info = {'status': True}

        return JsonResponse(ajax_success_info)
    else:
        catagory_info = Catagory.objects.all()
        every_page_num = 4  # 每页显示的记录数  #不加 order by 会有警告信息
        p = Paginator(Catagory.objects.all().order_by('-id', ), every_page_num)

        ##前端点击的page,第几页
        page = request.GET.get('page')

        # 当前页第一个文章的编号
        if page == None:
            page = 1
        current_page_first = (int(page) - 1) * every_page_num

        try:
            page_obj = p.page(page)

        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            page_obj = p.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            page_obj = p.page(p.num_pages)
        return render(request, 'backend/catagory_admin.html', context={
            'page_obj': page_obj, 'current_page_first': current_page_first,
            'catagory_info': catagory_info,
        })


def comment_admin(request):
    if request.POST:
        print(request.POST)
        catagory_id = request.POST.get('key_post')
        catagory_name = request.POST.get('value_post')

        update_obj = Catagory.objects.get(id=int(catagory_id))
        update_obj.name = catagory_name
        update_obj.save()

        ajax_success_info = {'status': True}

        return JsonResponse(ajax_success_info)
    else:

        every_page_num = 4  # 每页显示的记录数  #不加 order by 会有警告信息
        p = Paginator(Comment.objects.all().order_by('-publish_time', ), every_page_num)

        ##前端点击的page,第几页
        page = request.GET.get('page')

        # 当前页第一个文章的编号
        if page == None:
            page = 1
        current_page_first = (int(page) - 1) * every_page_num

        try:
            page_obj = p.page(page)

        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            page_obj = p.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            page_obj = p.page(p.num_pages)
        return render(request, 'backend/comment_admin.html', context={
            'page_obj': page_obj, 'current_page_first': current_page_first,
        })
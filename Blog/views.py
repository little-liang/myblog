from django.shortcuts import render

# Create your views here.
from Blog.models import *
import markdown
def index(request):

    return render(request, 'index.html')

def admin1(request):

    article_list = Article.objects.all()
    print(article_list)
    return render(request, 'admin1.html', context={'article_list': article_list})

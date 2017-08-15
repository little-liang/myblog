from django.shortcuts import render

# Create your views here.
from Blog.models import Article
import markdown
def index(request):

    return render(request, 'index.html')

def admin1(request):


    article_list = Article.objects.all()

    return render(request, 'admin1.html', context={'article_list': article_list})

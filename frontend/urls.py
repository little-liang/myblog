from django.conf.urls import url
from frontend import views

urlpatterns = [
    url(r'^category.html$', views.category, name='category'),
    url(r'^article/(?P<article_id>\d+).html$', views.test),
]

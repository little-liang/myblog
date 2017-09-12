from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^article_admin.html$', article_admin, name='article_admin'),
    url(r'^tags_admin.html$', tags_admin, name='tags_admin'),
    url(r'^edit_article.html$', edit_article, name='edit_article'),
    url(r'^submit_article_id.html$', submit_article_id, name='submit_article_id'),
]

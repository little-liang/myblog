"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from frontend.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    url(r'^404.html$', error, name='error'),
    url(r'^readers.html$', readers, name='readers'),
    url(r'^tags.html$', tags, name='tags'),
    url(r'^article.html$', article, name='article'),
    url(r'^links.html$', links, name='links'),
    url(r'^UpgradeBrowser.html$', UpgradeBrowser, name='UpgradeBrowser'),
    url(r'^backend/', include('backend.urls')),
    url(r'^frontend/', include('frontend.urls')),
]

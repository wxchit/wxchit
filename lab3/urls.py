"""lab3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from bookdb.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/$', Search_form),
    url(r'^search_result/$', Search),
    url(r'^views/$', book_views),
    url(r'^delete/$', Delete),
    url(r'^update/$', update),
    url(r'^add_form/$', add_form),
    url(r'^add/$', Add),
    #url(r'^tip/$', Tip),
    url(r'^add_author/$', add_author),
]

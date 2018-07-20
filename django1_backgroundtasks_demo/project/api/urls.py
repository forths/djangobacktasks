# -*- coding:utf-8 -*-
from django.conf.urls import url
from . import views
 
urlpatterns = [
    url(r'^$', views.index), #这里 r'^$' 里面得加上 ^$ 。如果里面还要配置 URL 结尾记的加上反斜杠，如 r'^index/$'
    url(r'^upload/$',views.upload,name='upload'),
]

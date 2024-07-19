from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # re_path(r'^articles/$', views.article_list),
    # re_path(r'^articles/(?P<pk>[0-9]+)$', views.article_detail),
    re_path(r'^articles/$', views.ArticleList.as_view()),
    re_path(r'^articles/(?P<pk>[0-9]+)$', views.ArticleDetail.as_view()),
    re_path(r'home', views.index),
    re_path(r'chat_part', views.chat_part, name='chat_part'),
    re_path(r'chat_room', views.chat_teac, name='chat_room'),
    re_path(r'data_increase', views.data_increase),

]

urlpatterns = format_suffix_patterns(urlpatterns)

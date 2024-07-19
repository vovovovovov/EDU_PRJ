from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from API.BlueLM_api import sync_vivogpt
from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
import json


class ArticleList(APIView):
    """
    List all articles, or create a new article.
    """

    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            # 注意：手动将request.user与author绑定
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ArticleDetail(APIView):
    """
    Retrieve, update or delete an article instance.
    """

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        article = self.get_object(pk)
        serializer = ArticleSerializer(instance=article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create your views here.
def index(request):
    print("try to connect")
    data = {
        'title': '科技文献大模型',

    }
    return render(request, 'mmmm.html', data)


def chat(request):
    context = {
        'title': 'a main view'
    }

    return render(request, 'main.html', context)


# TODO  主页面
'''
    主页面: http://127.0.0.1:8000
'''


def main_page(request):
    return render(request, 'main_page.html')


# TODO 对话功能交互实现
'''
    接受参数：用户提出的问题
    返回参数：回答
'''


def chat_part(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message')
        if user_message:
            response = sync_vivogpt(user_message, '系统提示', 0.7)  # 根据需要传递参数
            return JsonResponse({'response': response})
    return render(request, 'main.html', {'initial_message': '您好！我是智海小助手，很高兴为您服务。请问有什么可以帮您解决的问题吗？'})


def data_increase(request):
    """使用sqlite3添加数据"""
    
    return None


def chat_teac(request):

    return HttpResponse("OK")
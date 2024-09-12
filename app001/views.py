from django.shortcuts import render, HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from .models import Article
from .serializers import ArticleSerializer
from django.http import JsonResponse
import json

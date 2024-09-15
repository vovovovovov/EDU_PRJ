from django.urls import include, path
from rest_framework import routers
from .views import ChatSessionViewSet, MessageViewSet, GenerateReplyView

router = routers.DefaultRouter()
router.register(r'chat-sessions', ChatSessionViewSet)
router.register(r'messages', MessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('generate-reply/', GenerateReplyView.as_view(), name='generate-reply'),
]

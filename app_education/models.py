from django.db import models

# Create your models here.
class ChatSession(models.Model):
    title = models.CharField(max_length=255)   # 标题
    created_at = models.DateTimeField(auto_now_add=True)   # 时间

class Message(models.Model):
    chat_session = models.ForeignKey(ChatSession, related_name='messages', on_delete=models.CASCADE)
    sender = models.CharField(max_length=10)  # 'user' 或 'ai'
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
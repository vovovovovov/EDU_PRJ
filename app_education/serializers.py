# chat/serializers.py
from rest_framework import serializers
from .models import ChatSession, Message

"""
使用了Django REST Framework（DRF）来为ChatSession和Message两个模型创建序列化器（serializer）。
序列化器的作用是将复杂的数据类型（如Django模型实例）转换为Python的基本数据类型（如字典、列表），这样就
可以轻松地将数据序列化为JSON等格式，从而进行数据的传输或存储。序列化器也可以用于从用户请求中解析数据，转
换回复杂的Django模型实例。
"""
class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ChatSessionSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatSession
        fields = ['id', 'title', 'created_at', 'messages']

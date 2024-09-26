from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import ChatSession, Message
from .serializers import MessageSerializer, ChatSessionSerializer
# 大模型接口导入
from API.llm_api import llm_api


# 聊天序列化
class ChatSessionViewSet(viewsets.ModelViewSet):
    queryset = ChatSession.objects.all().order_by('-created_at')
    serializer_class = ChatSessionSerializer

# 聊天信息序列化
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer



# 回复生成
class GenerateReplyView(APIView):
    def post(self, request):
        chat_session_id = request.data.get('chat_session')
        user_message = request.data.get('content')

        if not chat_session_id or not user_message:
            return Response({'error': '缺少必要的参数'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            chat_session = ChatSession.objects.get(id=chat_session_id)
        except ChatSession.DoesNotExist:
            return Response({'error': '聊天会话不存在'}, status=status.HTTP_404_NOT_FOUND)

        # 保存用户消息
        user_message_obj = Message.objects.create(
            chat_session=chat_session,
            sender='user',
            content=user_message
        )

        # 调用 AI 模型生成回复
        ai_reply_content = llm_api(user_message)

        # 保存 AI 回复消息
        ai_message_obj = Message.objects.create(
            chat_session=chat_session,
            sender='ai',
            content=ai_reply_content
        )

        # 返回 AI 回复
        serializer = MessageSerializer(ai_message_obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# 题目生成
class Generate_questions_view(APIView):
    def post(self ,request):
        prompt = request.data.get('prompt', '')

        # 检测
        if not prompt:
            return Response({"error": "请提供提示内容！"}, status=status.HTTP_400_BAD_REQUEST)

        # llm生成
        selected_questions = llm_api(prompt)

        return Response(selected_questions, status=status.HTTP_200_OK)


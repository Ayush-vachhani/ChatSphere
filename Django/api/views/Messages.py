from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

# model and serializers
from api.models import Chat
class MessageView(APIView):
    @staticmethod
    def post(request):
        user1_name = request.data.get('user1_name')
        user2_name = request.data.get('user2_name')
        # sort the names
        user1_name, user2_name = sorted([user1_name, user2_name])
        # get the chat object
        chat, created = Chat.objects.get_or_create(user1_name=user1_name, user2_name=user2_name)
        print(chat.messages[0])
        return Response({'messages': chat.messages})
    
    @staticmethod
    def get(request):
        return Response({'messages': 'Failed'})

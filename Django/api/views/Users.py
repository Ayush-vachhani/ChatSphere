from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

# model and serializers
from api.models import UserNames
class UsersView(APIView):
    @staticmethod
    def post(request):
        # user1_name = request.data.get('user1_name')
        # user2_name = request.data.get('user2_name')
        # messageResponse = request.data.get('message')
        # sender = messageResponse['sender']
        # message = messageResponse['message']

        # user1_name, user2_name = sorted([user1_name, user2_name])
        # chat, created = Chat.objects.get_or_create(user1_name=user1_name, user2_name=user2_name)

        # # append the new message to the existing messages list
        # chat.messages.append({'sender': sender, 'message': message})
        # chat.save()
        return Response({'messages': 'success'})
    
    @staticmethod
    def get(request):
        usernames = UserNames.objects.all()
        usernames_list = [username.full_name for username in usernames]
        return Response({'UserNames': usernames_list})

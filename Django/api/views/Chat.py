from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

# model and serializers
from api.models import Signup

#mongodb database
import pymongo
client = pymongo.MongoClient()  # local instance of MongoDB
db = client.chatapp  # database name
collection = db.groups  # collection name

#websockets
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

class ChatView(APIView):
    @staticmethod
    def post(request):
        name = request.data.get('name')
        message = request.data.get('message')
        document = {'name': name, 'message': message}
        collection.update_one(
            {},
            {'$push': {'text': document}}
        )
        return Response({'message': 'Message created'})    

    @staticmethod
    def get(request):
        documents = collection.find({"text": {"$type": "array"}})  # filter the documents
        messages = [doc['text'] for doc in documents]  # extract the text field from each document
        return Response({'messages': messages})

    @staticmethod
    def delete(request):
        to_del = request.data.get('val')
        collection.update_one(
            {},
            {'$pull': {'text': {'message': to_del}}},
        )
        return Response({'message': 'Todo deleted'})
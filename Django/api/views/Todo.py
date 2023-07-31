# DRF
from rest_framework.views import APIView
from rest_framework.response import Response

# import apps for faster loads
from django.apps import apps

app = apps.get_app_config('api')
collection = app.collection


class TodoView(APIView):
    @staticmethod
    def post(request):
        todo = request.data.get('name')
        collection.update_one(
            {'name': 'arya'},
            {'$push': {'items': todo}}
        )
        return Response({'message': 'Todo created', 'res': todo})

    @staticmethod
    def get(request):
        document = collection.find_one({"name": "arya"})  # filter the document
        return Response({'message': document['items']})

    @staticmethod
    def delete(request):
        to_del = request.data.get('val')
        print(to_del)
        collection.update_one(
            {'name': 'arya'},
            {'$pull': {'items': to_del}}
        )
        return Response({'message': 'Todo deleted'})

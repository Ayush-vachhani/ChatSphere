from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Post  # Make sure to import your Post model
from api.serializers import PostSerializer

class PostView(APIView):
    @staticmethod
    def post(request):
        pass
    
    @staticmethod
    def get(request):
        posts = Post.objects.all()  # Fetch all posts using the Post model
        serializer = PostSerializer(posts, many=True)  # Serialize the fetched posts
        return Response({'posts': serializer.data})  # Return the serialized data

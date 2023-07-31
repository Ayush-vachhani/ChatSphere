from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

# model and serializers
from api.models import Signup
from api.serializers import SignupSerializer

# for posting data
from django.middleware.csrf import get_token


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        if Signup.objects.filter(email=email, password=password).exists():
            user = Signup.objects.get(email=email)
            serializer = SignupSerializer(user)
            return Response({'message': 'Login successful', 'email': user.email, 'user': serializer.data},
                            status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)

    def get(self, request):
        query_params = request.GET.dict()
        info = Signup.objects.filter(**query_params)
        serializer = SignupSerializer(info, many=True)
        return Response(serializer.data)

    def patch(self, request):
        email = request.data.get('email')
        isloggedin = request.data.get('isloggedin')
        if Signup.objects.filter(email=email).exists():
            user = Signup.objects.get(email=email)
            user.isloggedin = isloggedin
            user.save()
            return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

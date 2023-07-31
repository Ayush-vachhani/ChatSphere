from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status

# model and serializers
from api.models import Signup
from api.serializers import SignupSerializer

# for posting data
from django.middleware.csrf import get_token


class SignupView(APIView):
    def post(self, request):
        csrf_token = get_token(request)
        self.request.session.create()
        serializer = SignupSerializer(data=request.data, context={'csrf_token': csrf_token, 'request': request})
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if Signup.objects.filter(email=email).exists():
                return Response({'error': 'User already exists', 'token': 1234}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        query_params = request.GET.dict()
        info = Signup.objects.filter(**query_params)  # type: ignore
        serializer = SignupSerializer(info, many=True)
        return Response(serializer.data)

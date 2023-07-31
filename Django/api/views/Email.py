from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import serializers
from rest_framework import status

# model and serializers
from api.models import Signup

# sending email
from django.core.mail import send_mail
# from django.conf import settings


class EmailView(APIView):
    @staticmethod
    def post(request):
        to_email = request.data.get('to_email')
        user = Signup.objects.get(email=to_email)
        user_name = user.name
        user_last_name = user.last_name
        message = f'Dear {user_name} {user_last_name}\n\nThank you for subscribing to b-kart! We are thrilled to have '\
                  f'you on board and ' \
                  f'can\'t wait to share our latest products and promotions with you.\n\nAs a subscriber, you will be '\
                  f'the first to know about our new arrivals, exclusive discounts, and special offers. We promise to ' \
                  f'keep your inbox clutter-free and only send you the most relevant content.\n\nIf you have any ' \
                  f'questions or feedback, please do not hesitate to reach out to us .\n\nThank you again for ' \
                  f'subscribing, and we hope you enjoy shopping with us!\n\nBest regards,\nB-kart Team.'
        print(request.data)
        send_simple_message(to_email, message)
        # if response.status_code == 200:
        #     return Response({'message': 'Email sent successfully'}, status=status.HTTP_200_OK)
        # else:
        #     return Response({'error': 'Mail has been sent'}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def get(request):
        return Response({'message': 'Figuring it out..'}, status=status.HTTP_200_OK)


def send_simple_message(email, message):
    send_mail(
        'Welcome to B-kart',  # sub
        message,
        'settings.EMAIL_HOST_USER',  # sender
        [email],  # receiver
        fail_silently=False,
    )

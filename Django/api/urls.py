from django.urls import path,re_path

# Signup view
from .views.Signup import SignupView
# Login view
from .views.Login import LoginView
# Users view
from .views.Users import UsersView
# Messages view
from .views.Messages import MessageView
urlpatterns = [
    path('signup', SignupView.as_view(), name="signup"),
    path('login', LoginView.as_view(), name="login"),
    path('users', UsersView.as_view(), name="users"),
    path('messages', MessageView.as_view(), name="messages"),
]
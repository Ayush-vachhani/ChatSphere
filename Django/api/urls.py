from django.urls import path,re_path

# Signup view
from .views.Signup import SignupView
# Login view
from .views.Login import LoginView
# Email view
from .views.Email import EmailView
# Todo view
from .views.Todo import TodoView
# Chat view
from .views.Chat import ChatView

urlpatterns = [
    path('signup', SignupView.as_view(), name="signup"),
    path('login', LoginView.as_view(), name="login"),
    path('email', EmailView.as_view(), name="email"),
    path('todo', TodoView.as_view(), name="todo"),
    path('chat', ChatView.as_view(), name="chat"),
]
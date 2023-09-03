from django.contrib import admin

# Register your models here.
from .models import Signup
from .models import Chat
from .models import UserNames
from .models import Post

admin.site.register(Signup)
admin.site.register(Chat)
admin.site.register(UserNames)
admin.site.register(Post)

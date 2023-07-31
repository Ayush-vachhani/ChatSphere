from django.contrib import admin

# Register your models here.
from .models import Information
from .models import Signup

admin.site.register(Information)
admin.site.register(Signup)

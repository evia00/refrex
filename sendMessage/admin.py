from django.contrib import admin

# Register your models here.
from django.contrib import admin
from sendMessage.models import Message

admin.site.register(Message)
from django.contrib import admin
from .models import User, Lang, Message, Prof


# Register your models here.
admin.site.register([User, Lang, Message, Prof])

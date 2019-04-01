from django.shortcuts import render
from .models import User, Lang, Prof, Message
from .serializers import (
    UserSerializer,
    LangSerializer,
    ProfSerializer,
    MessageSerializer,
)
from rest_framework import viewsets
from django.http import JsonResponse

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LangView(viewsets.ModelViewSet):
    queryset = Lang.objects.all()
    serializer_class = LangSerializer


class ProfView(viewsets.ModelViewSet):
    queryset = Prof.objects.all()
    serializer_class = ProfSerializer


class MessageView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

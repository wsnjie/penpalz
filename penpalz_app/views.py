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
from django.db.models import Avg
from rest_framework.response import Response
from rest_framework import serializers

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LangView(viewsets.ModelViewSet):
    queryset = Lang.objects.all()
    serializer_class = LangSerializer

    def get_queryset(self):
        return Lang.objects.annotate(avg_level=Avg("prof_of_lang__level"))


class ProfView(viewsets.ModelViewSet):
    queryset = Prof.objects.all()
    serializer_class = ProfSerializer


class MessageView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request):
        data = request.data
        s = MessageSerializer(data=data)
        s.is_valid()
        print(s.data)
        print(s.data["sent"])
        sent_prof = Prof.objects.filter(
            user=data["sent"], language=data["language"]
        ).values("level")
        rec_prof = Prof.objects.filter(
            user=data["rec"], language=data["language"]
        ).values("level")
        sent_level = sent_prof[0]["level"]
        rec_level = rec_prof[0]["level"]
        check = abs(sent_level - rec_level)
        if check <= 2:
            new_message = Message.objects.create(
                sent=User.objects.get(pk=s.data["sent"]),
                rec=User.objects.get(pk=s.data["rec"]),
                language=Lang.objects.get(pk=s.data["language"]),
                content=s.data["content"],
            )

            new_message.save()
            return Response(s.data)
        return Response("Proficiency Mismatch")

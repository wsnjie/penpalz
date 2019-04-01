from rest_framework import serializers
from .models import User, Lang, Prof, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class LangSerializer(serializers.ModelSerializer):

    avg_level = serializers.ReadOnlyField()

    class Meta:
        model = Lang
        fields = "__all__"


class ProfSerializer(serializers.ModelSerializer):
    prof_of_user = UserSerializer(read_only=True)
    prof_of_lang = LangSerializer(read_only=True)

    class Meta:
        model = Prof
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    from_user = UserSerializer(read_only=True)
    to_user = UserSerializer(read_only=True)
    in_language = LangSerializer(read_only=True)

    class Meta:
        model = Message
        fields = "__all__"

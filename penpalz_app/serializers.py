from rest_framework import serializers
from .models import User, Lang, Prof, Message


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class MessageUserSerializer(serializers.ModelSerializer):
    from_user = UserSerializer()

    class Meta:
        model = User
        fields = "__all__"


class LangSerializer(serializers.ModelSerializer):

    avg_level = serializers.ReadOnlyField()

    class Meta:
        model = Lang
        fields = "__all__"


class ProfSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    language = LangSerializer(read_only=True)

    class Meta:
        model = Prof
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


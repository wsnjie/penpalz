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
    user = UserSerializer(read_only=True)
    language = LangSerializer(read_only=True)

    class Meta:
        model = Prof
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    sent = UserSerializer(read_only=True)
    rec = UserSerializer(read_only=True)
    language = LangSerializer(read_only=True)

    sent_prof = serializers.SerializerMethodField()
    rec_prof = serializers.SerializerMethodField()

    class Meta:
        model = Message
        fields = "__all__"

    def get_sent_prof(self, obj):
        prof = Prof.objects.filter(user=obj.sent.id, language=obj.language.id).values(
            "level"
        )
        return prof

    def get_rec_prof(self, obj):
        prof = Prof.objects.filter(user=obj.rec.id, language=obj.language.id).values(
            "level"
        )
        return prof

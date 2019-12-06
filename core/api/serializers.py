from rest_framework import serializers

from core.models import Profile, Emotion, Statement


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("id", "user", "comment", "nickname", "gender")
        read_only_fields = ("id", "user")


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = (
            "id",
            "user",
            "anger",
            "contempt",
            "disgust",
            "fear",
            "happiness",
            "neutral",
            "sadness",
            "surprise",
            "main_emotion",
            "image_url",
            "comment",
            "created_at",
        )
        read_only_fields = ("id", "user", "created_at",)


class StatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
        fields = ("user", "text", "category")

from rest_framework import serializers

from core.models import Profile, Emotion, Picture, Statement


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("uid", "email", "name", "nickname", "gender")


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emotion
        fields = (
            "user",
            "anger",
            "contempt",
            "disgust",
            "fear",
            "happiness",
            "neutral",
            "sadness",
            "surprise",
            "created_at",
        )
        read_only_fields = ("created_at",)


class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ("user", "url", "created_at")
        read_only_fields = ("created_at",)


class StatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statement
        fields = ("user", "text", "category")

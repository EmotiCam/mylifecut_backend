from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHER = "OTHER"
    SECRET = "SECRET"
    GENDER_CHOICES = [
        (MALE, "남자"),
        (FEMALE, "여자"),
        (OTHER, "OTHER"),
        (SECRET, "SECRET"),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    name = models.CharField(max_length=30, null=False)
    nickname = models.CharField(max_length=30, null=False)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)


class Emotion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anger = models.FloatField()
    contempt = models.FloatField()
    disgust = models.FloatField()
    fear = models.FloatField()
    happiness = models.FloatField()
    neutral = models.FloatField()
    sadness = models.FloatField()
    surprise = models.FloatField()
    main_emotion = models.CharField(max_length=15)
    image_url = models.URLField()
    comment = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)


class Statement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    text = models.CharField(max_length=100)
    category = models.CharField(max_length=10)
    default = models.BooleanField(default=False)

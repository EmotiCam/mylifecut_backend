import json
import random

from django.db import connection
from django.utils import timezone
from datetime import datetime, timedelta

from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from core.api.serializers import (
    ProfileSerializer,
    EmotionSerializer,
    StatementSerializer,
)
from core.models import Profile, Emotion, Statement


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EmotionViewSet(viewsets.ModelViewSet):
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class StatementViewSet(viewsets.ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer
    permission_classes = (AllowAny,)

    @action(detail=False, methods=["GET"], url_path="anger")
    def anger(self, request):
        neutral = Statement.objects.filter(category="anger")
        serializer = self.get_serializer(neutral, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"], url_path="contempt")
    def contempt(self, request):
        neutral = Statement.objects.filter(category="contempt")
        serializer = self.get_serializer(neutral, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"], url_path="disgust")
    def disgust(self, request):
        neutral = Statement.objects.filter(category="disgust")
        serializer = self.get_serializer(neutral, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"], url_path="fear")
    def fear(self, request):
        neutral = Statement.objects.filter(category="fear")
        serializer = self.get_serializer(neutral, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"], url_path="happiness")
    def happiness(self, request):
        neutral = Statement.objects.filter(category="happiness")
        serializer = self.get_serializer(neutral, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"], url_path="neutral")
    def neutral(self, request):
        neutral = Statement.objects.filter(category="neutral")
        serializer = self.get_serializer(neutral, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"], url_path="sadness")
    def sadness(self, request):
        neutral = Statement.objects.filter(category="sadness")
        serializer = self.get_serializer(neutral, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=False, methods=["GET"], url_path="surprise")
    def surprise(self, request):
        neutral = Statement.objects.filter(category="surprise")
        serializer = self.get_serializer(neutral, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SympathyWords(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        with open("data/words.json") as word_json:
            words = json.load(word_json)
        return_sympathy_word = random.choice(words["sympathy"])

        response_builder = {
            "version": "2.0",
            "resultCode": "OK",
            "output": {"return_sympathy_word": return_sympathy_word},
        }
        return Response(response_builder)


class ConsolationWords(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        with open("data/words.json") as word_json:
            words = json.load(word_json)
        return_consolation_word = random.choice(words["consolation"])

        response_builder = {
            "version": "2.0",
            "resultCode": "OK",
            "output": {"return_consolation_word": return_consolation_word},
        }
        return Response(response_builder)


class PeriodEmotion(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        last_url = request.get_full_path().split("/")[-1]
        if last_url == "today-emotion":
            day_ago = 0
        else:
            day_ago = 6

        cursor = connection.cursor()
        cursor.execute(
            f"""
            SELECT AVG(anger)     fear,
                   AVG(contempt)  contempt,
                   AVG(disgust)   disgust,
                   AVG(fear)      fear,
                   AVG(happiness) happiness,
                   AVG(neutral)   neutral,
                   AVG(sadness)   sadness,
                   AVG(surprise)  surprise,
                   COUNT(id)      count
            FROM core_emotion
            WHERE created_at > {timezone.localdate() - timedelta(days=day_ago)}
              AND user_id = 32
        """
        )
        emotion_types = ["화남", "짜증", "역겨움", "걱정", "행복 ", "평온함", "슬픔", "놀라움"]
        row = cursor.fetchone()
        count = row[-1]
        emotion_pair = list(zip([int(i * 100) for i in row[:-1]], emotion_types))
        emotion_pair.sort(reverse=True)

        if day_ago == 0:
            response_builder = {
                "version": "2.0",
                "resultCode": "OK",
                "output": {
                    "return_emotion_name": emotion_pair[0][1],
                    "return_emotion_portion": emotion_pair[0][0],
                },
            }
        else:
            response_builder = {
                "version": "2.0",
                "resultCode": "OK",
                "output": {
                    "return_emotion_name1": emotion_pair[0][1],
                    "return_emotion_portion1": emotion_pair[0][0],
                    "return_emotion_name2": emotion_pair[1][1],
                    "return_emotion_portion2": emotion_pair[1][0],
                    "return_emotion_name3": emotion_pair[2][1],
                    "return_emotion_portion3": emotion_pair[2][0],
                    "return_emotion_counts": count,
                },
            }
        return Response(response_builder)

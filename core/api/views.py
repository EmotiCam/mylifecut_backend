from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.api.serializers import (
    ProfileSerializer,
    EmotionSerializer,
    PictureSerializer,
    StatementSerializer,
)
from core.models import Profile, Emotion, Picture, Statement


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)


class EmotionViewSet(viewsets.ModelViewSet):
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer
    permission_classes = (IsAuthenticated,)


class PictureViewSet(viewsets.ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer
    permission_classes = (IsAuthenticated,)


class StatementViewSet(viewsets.ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer
    permission_classes = (IsAuthenticated,)

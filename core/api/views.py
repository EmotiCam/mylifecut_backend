from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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


class EmotionViewSet(viewsets.ModelViewSet):
    queryset = Emotion.objects.all()
    serializer_class = EmotionSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        """Create a new profile"""
        serializer.save(user=self.request.user)


class StatementViewSet(viewsets.ModelViewSet):
    queryset = Statement.objects.all()
    serializer_class = StatementSerializer
    permission_classes = (IsAuthenticated,)

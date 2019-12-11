from django.urls import path
from rest_framework.routers import DefaultRouter

from core.api import views

# namespace
app_name = "core"

urlpatterns = [
    path("consolation-words", views.ConsolationWords.as_view()),
    path("sympathy-words", views.SympathyWords.as_view()),
    path("period-emotion", views.PeriodEmotion.as_view()),
    path("today-emotion", views.PeriodEmotion.as_view()),
    path("seven-days-emotion", views.PeriodEmotion.as_view()),
]

router = DefaultRouter()
router.register("profiles", views.ProfileViewSet)
router.register("emotions", views.EmotionViewSet)
router.register("statements", views.StatementViewSet)

urlpatterns += router.urls

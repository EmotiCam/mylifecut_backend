from rest_framework.routers import DefaultRouter

from core.api import views

# namespace
app_name = "core"

router = DefaultRouter()
router.register("profiles", views.ProfileViewSet)
router.register("emotions", views.EmotionViewSet)
router.register("statements", views.StatementViewSet)

urlpatterns = router.urls

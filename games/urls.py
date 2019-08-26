from django.urls import path
from rest_framework.routers import DefaultRouter

from games.views import GameModelViewSet

app_name = "games"

router = DefaultRouter()
router.register("games", GameModelViewSet)

urlpatterns = router.urls

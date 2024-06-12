from django.urls import include, path
from rest_framework.routers import SimpleRouter

from src.member import apis

router = SimpleRouter()
router.register("members", apis.MemberViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

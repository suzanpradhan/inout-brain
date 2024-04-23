from django.urls import include, path
from rest_framework.routers import SimpleRouter

from src.employee import apis

router = SimpleRouter()
router.register("employees", apis.EmployeeViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

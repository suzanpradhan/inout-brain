from django.urls import path
from django.views.decorators.http import require_GET

from src.general import apis

urlpatterns = [
    path("is-data-updated", apis.GetIsUpdatedAPI.as_view(), name="get_is_data_updated"),
    path(
        "general",
        apis.GeneralAPISet.as_view({"get": "list"}),
        name="get_general",
    ),
    path(
        "general/",
        apis.GeneralAPISet.as_view({"patch": "update"}),
        name="get_general",
    ),
    # path("general", apis.GeneralAPISet, name="update_general"),
]

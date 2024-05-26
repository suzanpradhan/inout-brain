from django.urls import path

from src.general import apis

urlpatterns = [
    path("is-data-updated", apis.GetIsUpdatedAPI.as_view(), name="get_is_data_updated"),
    path("general", apis.GetGeneralAPI.as_view(), name="get_general"),
]

from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from src.general.models import General
from src.general.serializers import IsDataUpdatedSerializer


class GetIsUpdatedAPI(generics.GenericAPIView):
    """
    Get Update Data API
    """

    serializer_class = IsDataUpdatedSerializer
    queryset = General.objects.all()
    pagination_class = None
    permission_classes = [IsAuthenticated]
    http_method_names = ("get",)

    def get(self, request) -> Response:
        """
        Handle Get Request
        """

        serializer = self.serializer_class(data=request.data)

        serializer = self.get_serializer(self.queryset.first(), data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data)

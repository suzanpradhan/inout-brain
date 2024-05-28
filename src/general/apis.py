from rest_framework import generics, viewsets
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from src.general.models import General
from src.general.serializers import GeneralSerializer, IsDataUpdatedSerializer


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


class GetGeneralAPI(generics.GenericAPIView):
    serializer_class = GeneralSerializer
    queryset = General.objects.all()
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


class GeneralAPISet(viewsets.ModelViewSet):
    serializer_class = GeneralSerializer
    queryset = General.objects.all()
    permission_classes = [IsAuthenticated, IsAdminUser]
    lookup_field = "pk"
    http_method_names = ("get", "post", "patch", "delete")

    def get_object(self):
        return self.get_queryset().first()

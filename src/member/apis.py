from rest_framework import viewsets

from src.member.models import Member
from src.member.serializers import MemberOrderSerializer, MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    """
    Model View Set for Member
    """

    serializer_class = MemberSerializer
    queryset = Member.objects.all().order_by("order")
    permission_classes = []
    lookup_field = "pk"
    http_method_names = ("get", "post", "patch", "delete")

    def get_serializer_class(self):
        if self.action == "update_order":
            return MemberOrderSerializer
        return super().get_serializer_class()

from django.db import transaction
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from src.employee.models import Employee
from src.employee.serializers import EmployeeOrderSerializer, EmployeeSerializer
from src.general.models import General


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Model View Set for Employee
    """

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all().order_by("order")
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"
    http_method_names = ("get", "post", "patch", "delete")

    def get_serializer_class(self):
        if self.action == "update_order":
            return EmployeeOrderSerializer
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        General.objects.all().update(is_data_updated=False)
        return super().list(request, *args, **kwargs)

    @action(detail=True, methods=["patch"])
    def refresh(self, request, *args, **kwargs):
        General.objects.all().update(is_data_updated=True)
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        method="patch",
        request_body=EmployeeOrderSerializer(many=True),
    )
    @action(detail=False, methods=["patch"])
    def update_order(self, request):
        serializer = self.get_serializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        employees_obj_for_update = []

        with transaction.atomic():
            for item in data:
                employee = Employee.objects.get(id=item["id"])
                employee.order = item["order"]
                employees_obj_for_update.append(employee)

            Employee.objects.bulk_update(employees_obj_for_update, ["order"])
            General.objects.all().update(is_data_updated=True)

        return Response({"status": "Order updated"})

    @action(detail=False, methods=["get"])
    def all(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from src.employee.models import Employee
from src.employee.serializers import EmployeeSerializer
from src.general.models import General


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Model View Set for Employee
    """

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"
    http_method_names = ("get", "post", "patch", "delete")

    def list(self, request, *args, **kwargs):
        General.objects.all().update(is_data_updated=False)
        return super().list(request, *args, **kwargs)

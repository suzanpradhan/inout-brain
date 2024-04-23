from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from src.employee.models import Employee
from src.employee.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Model View Set for Employee
    """

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    pagination_class = None
    permission_classes = [IsAuthenticated]
    lookup_field = "pk"
    http_method_names = ("get", "post", "patch", "delete")

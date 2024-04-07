from rest_framework import serializers

from src.employee.models import Employee, Position


class PositionSerializer(serializers.Serializer):
    """
    Serializer for Profile
    """

    class Meta:
        """
        Meta Class
        """

        model = Position
        fields = "__all__"

class EmployeeSerializer(serializers.Serializer):
    """
    Serializer for Profile
    """

    class Meta:
        """
        Meta Class
        """

        model = Employee
        fields = "__all__"

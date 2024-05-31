from rest_framework import serializers

from src.employee.models import Employee, Position


class PositionSerializer(serializers.ModelSerializer):
    """
    Serializer for Profile
    """

    class Meta:
        """
        Meta Class
        """

        model = Position
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    """
    Serializer for Profile
    """

    class Meta:
        """
        Meta Class
        """

        model = Employee
        fields = "__all__"
        depth = 1


class EmployeeOrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    order = serializers.IntegerField(required=True)
    """
    Serializer for Employee Order
    """

    class Meta:
        model = Employee
        fields = ("id", "order")

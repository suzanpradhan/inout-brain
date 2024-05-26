from rest_framework import serializers

from src.general.models import General


class IsDataUpdatedSerializer(serializers.ModelSerializer):
    """
    Serializer for General
    """

    class Meta:
        """
        Meta Class
        """

        model = General
        fields = ("is_data_updated",)


class GeneralSerializer(serializers.ModelSerializer):
    """
    Serializer for General
    """

    class Meta:
        """
        Meta Class
        """

        model = General
        fields = "__all__"

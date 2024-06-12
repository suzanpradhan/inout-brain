from rest_framework import serializers

from src.member.models import Member


class MemberSerializer(serializers.ModelSerializer):
    """
    Serializer for Profile
    """

    class Meta:
        """
        Meta Class
        """

        model = Member
        fields = "__all__"
        depth = 1


class MemberOrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=True)
    order = serializers.IntegerField(required=True)
    """
    Serializer for Member Order
    """

    class Meta:
        model = Member
        fields = ("id", "order")

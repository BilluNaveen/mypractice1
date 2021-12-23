from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
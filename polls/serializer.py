from rest_framework import serializers
from .views import Question

class questionSerializer (serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"

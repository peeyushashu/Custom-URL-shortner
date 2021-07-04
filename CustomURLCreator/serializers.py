from rest_framework import serializers
from .models import CustomURL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomURL
        fields = '__all__'
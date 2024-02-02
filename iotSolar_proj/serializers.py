from rest_framework import serializers

from .models import DataSolar


class SolarDataSerializer(serializers.Serializer):
    class Meta:
        model = DataSolar
        fields= '__all__'




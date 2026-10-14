from rest_framework import serializers
from .models import Dueno

class DuenoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dueno
        fields = '__all__'
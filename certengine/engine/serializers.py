from rest_framework.serializers import ModelSerializer
from engine.models import Car

class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
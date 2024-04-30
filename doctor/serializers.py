from rest_framework import serializers
from . import models

class doctorSerializers(serializers.ModelSerializer):
    department=serializers.StringRelatedField(many=False)
    class Meta:
        model=models.Doctor
        fields="__all__"
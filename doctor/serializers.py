from rest_framework import serializers
from . import models

class doctorSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Doctor
        fields="__all__"
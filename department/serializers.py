from rest_framework import serializers
from . import models

class departmentSerializers(serializers.ModelSerializer):
    class Meta:
        model=models.Department
        fields="__all__"
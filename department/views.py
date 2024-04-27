from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers

# Create your views here.
class departmentViewset(viewsets.ModelViewSet):
    queryset = models.Department.objects.all()
    serializer_class = serializers.departmentSerializers
    
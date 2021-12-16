from rest_framework import serializers
from .models import Number
from rest_framework.renderers import JSONRenderer

class ExtensoSerializer(serializers.Serializer):
    extenso = serializers.CharField()


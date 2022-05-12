from rest_framework import serializers
from main.models import Processes

# choosing to only display processData instead of id and processData
class processesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processes
        fields = ['processData']
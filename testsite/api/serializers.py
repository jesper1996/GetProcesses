from rest_framework import serializers
from main.models import Processes

# choosing to only display name instead of id, name and for_delete
class processesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processes
        #fields = '__all__'
        fields = ['name']
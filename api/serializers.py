from rest_framework import serializers
from .models import *



class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'
        

class TrackingPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackingPackage
        fields = '__all__'
        
        


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"


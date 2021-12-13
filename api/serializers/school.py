from rest_framework import serializers
from ..models.school import School
from ..serializers.house import HouseSerializer

class SchoolSerializer(serializers.ModelSerializer):
    houses = HouseSerializer(many=True, read_only=True)
    # Define meta class
    class Meta:
        # Specify the model from which to define the fields
        model = School
        # Define fields to be returned
        fields = ('name', 'location', 'owner', 'houses')

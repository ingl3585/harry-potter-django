from rest_framework import serializers
from ..models.house import House
from ..serializers.student import StudentSerializer

class HouseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    # Define meta class
    class Meta:
        # Specify the model from which to define the fields
        model = House
        # Define fields to be returned
        fields = ('name', 'animal', 'slogan', 'school', 'students')

from rest_framework import serializers
from ..models.student import Student

class StudentSerializer(serializers.ModelSerializer):
    # Define meta class
    class Meta:
        # Specify the model from which to define the fields
        model = Student
        # Define fields to be returned
        fields = '__all__'

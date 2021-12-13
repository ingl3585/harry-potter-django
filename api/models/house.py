from django.db import models
from ..models.school import School

class House(models.Model):
    name = models.CharField(max_length=100)
    animal = models.CharField(max_length=100)
    slogan = models.CharField(max_length=100)
    school = models.ForeignKey(School, related_name='school', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.animal} {self.slogan} {self.school}"

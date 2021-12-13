from django.contrib import admin
from .models.school import School
from .models.house import House
from .models.student import Student
# Register your models here.
admin.site.register(School)
admin.site.register(House)
admin.site.register(Student)

from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.student import StudentSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.student import Student
from django.views import View
import json

# /books

class StudentsView(APIView):
    # POST /books/
    def post(self, request):
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response(student.data, status=status.HTTP_201_CREATED)
        else:
            return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET /books/
    def get(self, request):
        students = Student.objects.all()
        data = StudentSerializer(students, many=True).data
        return Response(data)

# /books/:id

class StudentView(APIView):
    # PATCH /books/:id/
    def patch(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        updated_student = StudentSerializer(student, data=request.data, partial=True)
        if updated_student.is_valid():
            updated_student.save()
            return Response(updated_student.data)

    # PUT /books/:id/
    def put(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        updated_student = StudentSerializer(student, data=request.data)
        if updated_student.is_valid():
            updated_student.save()
            return Response(updated_student.data)

    # DELETE /books/:id/
    def delete(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # GET /books/:id/
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        data = StudentSerializer(student).data
        return Response(data)

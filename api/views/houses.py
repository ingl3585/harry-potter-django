from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.house import HouseSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.house import House
from django.views import View
import json

# /books

class HousesView(APIView):
    # POST /books/
    def post(self, request):
        house = HouseSerializer(data=request.data)
        if house.is_valid():
            house.save()
            return Response(house.data, status=status.HTTP_201_CREATED)
        else:
            return Response(house.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET /books/
    def get(self, request):
        houses = House.objects.all()
        data = HouseSerializer(houses, many=True).data
        return Response(data)

# /books/:id

class HouseView(APIView):
    # PATCH /books/:id/
    def patch(self, request, pk):
        house = get_object_or_404(House, pk=pk)
        updated_house = HouseSerializer(house, data=request.data, partial=True)
        if updated_house.is_valid():
            updated_house.save()
            return Response(updated_house.data)

    # PUT /books/:id/
    def put(self, request, pk):
        house = get_object_or_404(House, pk=pk)
        updated_house = HouseSerializer(house, data=request.data)
        if updated_house.is_valid():
            updated_house.save()
            return Response(updated_house.data)

    # DELETE /books/:id/
    def delete(self, request, pk):
        house = get_object_or_404(House, pk=pk)
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # GET /books/:id/
    def get(self, request, pk):
        house = get_object_or_404(House, pk=pk)
        data = HouseSerializer(house).data
        return Response(data)

# api/views.py
from rest_framework import generics

from inventory import models
from . import serializers

class ListProduct(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers

class DetailProduct(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializers
from rest_framework import serializers
from inventory import models

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        fields = (
            'name',
            'type',
            'price',
            'specs',
            'quantity'
        )
        model = models.Product

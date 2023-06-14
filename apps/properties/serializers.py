from rest_framework import serializers
from apps.properties.models.property import Property



class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model =  Property
        fields = [
            'user_fk',
            'property_type',
            'adress',
            'price',
            'price_buyer',
            'price_seller',
            'size',
            'bedrooms',
            'availability',
            'image_url',
            'pk'
        ]
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "price",
            "description",
            "stock",
            "is_active",
            "created_at"
        ]

        read_only_fields = ['id', 'created-at']

    def validate_price(self,value):
        if value <= 0:
            raise serializers.ValidationError("Price Must Be greater than zero")
        return value

    def validate_stock(self, value):
        if value < 0:
            raise serializers.ValidationError('Price cannot be zero')
        if value > 10000:
            raise serializers.ValidationError('Stock cannot be greater than 10000')
        return value

    def validate(self, attrs):

        name = attrs.get('name')
        is_active = attrs.get('is_active')

        if name and "test" in name.lower():
            raise serializers.ValidationError({
                "name": "product name cannot contain the word test"
            })
        
        return attrs
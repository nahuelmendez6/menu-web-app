from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['id']
        exclude = ['local_owner']

        def validate_name(self, value):
            if Category.objects.filter(category_name=value).exists():
                raise serializers.ValidationError("Ya existe una categoría con el mismo nombra.")

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id']
        exclude = ['local_owner']

    def validate_name(self, value):
        if Product.objects.filter(product_name=value).exists():
            raise serializers.ValidationError("Ya existe un producto con el mismo nombra.")


    def validate_price(self, value):
        if value >= 0:
            raise serializers.ValidationError("El precio debe ser mayor a cer")

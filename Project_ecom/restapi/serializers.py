from rest_framework import serializers
from Ecom_app.models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields=['id', "category_name",]
        model = Category

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields=["id", "title", "desc", "category", "price", "quantity", "discount", "cash_on_delivery", "user"]
        model = Product
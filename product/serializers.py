from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from product.models import Product, ProductImage


class ProductImageDetailSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(
        max_length=None, use_url=True
    )

    class Meta:
        model = ProductImage
        fields = ['image']


class ProductDetailSerializer(serializers.ModelSerializer):
    product_images = ProductImageDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'variant', 'description', 'price',
                  'product_images']


class ProductListSerializer(serializers.ModelSerializer):
    product_images = SerializerMethodField()
    origin = SerializerMethodField()
    species = SerializerMethodField()
    roast_level = SerializerMethodField()
    tested = SerializerMethodField()
    processed = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'variant', 'origin', 'species',
                  'roast_level', 'tested', 'processed', 'description', 'price',
                  'product_images']

    @staticmethod
    def get_product_images(obj):
        items = ProductImage.objects.filter(product=obj)[:1]
        serializer = ProductImageDetailSerializer(instance=items, many=True)
        return serializer.data

    @staticmethod
    def get_origin(obj):
        if obj.origin:
            return obj.origin.name
        return ""

    @staticmethod
    def get_species(obj):
        if obj.species:
            return obj.species.name
        return ""

    @staticmethod
    def get_roast_level(obj):
        if obj.roast_level:
            return obj.roast_level.name
        return ""

    @staticmethod
    def get_tested(obj):
        if obj.tested:
            return obj.tested.name
        return ""

    @staticmethod
    def get_processed(obj):
        if obj.processed:
            return obj.processed.name
        return ""

from django_filters import FilterSet, RangeFilter

from django.http import Http404
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from product.serializers import ProductDetailSerializer, ProductListSerializer


# Create your views here.

class ProductListFilterSet(FilterSet):
    price = RangeFilter()

    class Meta:
        model = Product
        fields = ['origin', 'species', 'roast_level', 'tested', 'processed',
                  'price']

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.prefetch_related('product_images').all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductListSerializer
    filterset_class = ProductListFilterSet
    filterset_fields = ['origin', 'species', 'roast_level', 'tested',
                        'processed']
    ordering_fields = ['name', 'price']
    search_fields = ['name']

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Product.objects.prefetch_related('product_images').get(
                pk=pk)
        except Product.DoesNotExist:
            raise Http404

    # cache requested url for each user for 2 hours
    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)

# from django_filters import FilterSet, RangeFilter

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django_filters.filters import RangeFilter
from django_filters.rest_framework import FilterSet
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from product.models import Product
from product.serializers import ProductSerializer


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
    serializer_class = ProductSerializer
    filterset_class = ProductListFilterSet
    filterset_fields = ['origin', 'species', 'roast_level', 'tested',
                        'processed']
    ordering_fields = ['name', 'price']
    search_fields = ['name']

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.prefetch_related('product_images').all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

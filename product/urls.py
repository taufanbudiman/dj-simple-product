from django.urls import path

from product.views import ProductListView, ProductDetailView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product-list'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
]
from django.contrib import admin

from product.models import Product, ProductImage, Origin, Species, RoastLevel, \
    Tested, Processing

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Origin)
admin.site.register(Species)
admin.site.register(RoastLevel)
admin.site.register(Tested)
admin.site.register(Processing)

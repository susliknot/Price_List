from django.contrib import admin
from django.db import models
from .models import Product
from .models import Price


class PriceAdmin(admin.ModelAdmin):
    list_filter = ['price']
    search_fields = ['price']
admin.site.register(Price, PriceAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name']
admin.site.register(Product, ProductAdmin)


#class Meta:
#    abstract = True
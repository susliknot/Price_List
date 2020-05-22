from django.contrib import admin
from .models import Product

# from .models import Price

admin.site.register(Product)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter = ['name', 'price', 'date']
    search_fields = ['name', 'text']

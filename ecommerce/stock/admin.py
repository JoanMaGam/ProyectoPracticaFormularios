from django.contrib import admin
from .models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_description', 'stock',)
    search_fields = ('name', 'short_description',)
    list_filter = ('name', 'stock', 'discount_until',)
    date_hierarchy = 'discount_until'

admin.site.register(Product, ProductAdmin)

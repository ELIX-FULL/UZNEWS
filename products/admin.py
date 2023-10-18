from django.contrib import admin
from products.models import ProductModel, CategoryModel

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    search_fields = ['title']
    list_filter = ['created_at']





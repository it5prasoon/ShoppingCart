from django.contrib import admin

from .models import Category, Product, VariationColor, VariationSize


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    list_per_page = 20


admin.site.register(Product, ProductAdmin)
admin.site.register(VariationColor)
admin.site.register(VariationSize)

from django.contrib import admin

# Register your models here.
from goods.models import Categories, Products

# Register your models here.
# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ("name", "slug")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "price", "discount", "quantity", "category")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}

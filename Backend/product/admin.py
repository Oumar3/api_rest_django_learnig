from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price")
    list_filter = ["price"]
    list_per_page = 100
    list_max_show_all = 200
    search_fields =["name"]

admin.site.register(Product,ProductAdmin)
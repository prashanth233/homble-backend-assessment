from django.contrib import admin
from .models import Product
from products.models import Product
from .models import Product, Sku


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "selling_price", "managed_by")
    ordering = ("-id",)
    search_fields = ("name",)
    list_filter = ("is_refrigerated", "category")
    fields = (
        ("name", "selling_price"),
        ("category", "is_refrigerated"),
        "description",
        ("id", "created_at"),
        "managed_by",
    )
    autocomplete_fields = ("category", "managed_by")
    readonly_fields = ("id", "created_at")

class SkuInline(admin.TabularInline):
    model = Sku
    extra = 1

@admin.register(Sku)
class SkuAdmin(admin.ModelAdmin):
    list_display = ("product", "size", "selling_price")
    search_fields = ("product__name",)

class ProductInline(admin.StackedInline):
    """
    For display in CategoryAdmin
    """

    model = Product
    extra = 0
    ordering = ("-id",)
    readonly_fields = ("name", "selling_price", "is_refrigerated")
    fields = readonly_fields,
    show_change_link = True

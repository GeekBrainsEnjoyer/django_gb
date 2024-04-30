from django.contrib import admin

from .models import Product, Order, Client


class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'quantity']

    """Отдельный продукт."""
    readonly_fields = ['created_at']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name'],
            },
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Подробное описание товара',
                'fields': ['description'],
            },
        ),
        (
            'Бухгалтерия',
            {
                'fields': ['price', 'quantity'],
            }
        ),
        (
            'Прочее',
            {
                'fields': ['created_at'],
            }
        ),
    ]


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Client)

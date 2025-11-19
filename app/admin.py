from django.contrib import admin
from .models import Category, Product, Order, Comment
from django.utils.html import format_html
from django.urls import path
from django.shortcuts import redirect


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at')
    search_fields = ('title',)


@admin.action(description="Mark selected products as out of stock")
def mark_out_of_stock_action(modeladmin, request, queryset):
    queryset.update(stock=0)
    modeladmin.message_user(request, "Selected products are now out of stock!")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'price',
        'category',
        'is_in_stock',
        'stock',
        'image_preview',
        'created_at'
    )

    list_filter = ('category', 'created_at')
    search_fields = ('name',)
    readonly_fields = ('image_preview', 'created_at', 'updated_at')

    fieldsets = (
        ('Product Info', {
            'fields': ('name', 'description', 'price', 'discount', 'category')
        }),
        ('Stock', {
            'fields': ('stock',)
        }),
        ('Image', {
            'fields': ('image', 'image_preview')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
        }),
    )

    actions = [mark_out_of_stock_action]
    change_form_template = "admin/app/product/change_form.html"

    def is_in_stock(self, obj):
        return obj.stock > 0
    is_in_stock.boolean = True
    is_in_stock.short_description = "In Stock?"

    def image_preview(self, obj):
        if obj.image:
            return format_html(f'<img src="{obj.image.url}" width="70" style="border-radius: 6px;" />')
        return "No Image"
    image_preview.short_description = 'Image'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('<int:object_id>/mark_out_of_stock/', self.admin_site.admin_view(self.mark_out_of_stock), name='product-mark-out-of-stock'),
        ]
        return custom_urls + urls

    def mark_out_of_stock(self, request, object_id):
        product = self.get_object(request, object_id)
        product.stock = 0
        product.save()
        self.message_user(request, f"{product.name} is now out of stock!")
        return redirect(f'../../{object_id}/change/')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'quantity', 'status', 'created_at')
    list_filter = ('status', 'created_at')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'text', 'created_at')
    search_fields = ('text',)

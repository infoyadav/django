from django.contrib import admin

from .models import Product, Order, Category

from django.utils.html import format_html

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_id', 'cname']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("category","pname", "ptitle", "quantity", "image", 'price')
    search_fields = ('category',)
    list_filter = ('pname',)
    # search_fields = ('dob',)

    # this is used for we can see the image in admin panel
    # def image_tag(self, obj):
    #     return format_html('<img src="{}" />'.format(obj.image.url))
    # image_tag.short_description = 'image'

    # list_display = ("category","pname", "ptitle", "quantity", "image_tag")

    # fields = ['image_tag']
    # readonly_fields = ['image_tag']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', "product", "order_quantity", "date_of_order",)
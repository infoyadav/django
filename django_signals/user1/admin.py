from django.contrib import admin
from .models import User, Store

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo', 'description']

@admin.register(Store)
class StoreaAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'city', 'state']
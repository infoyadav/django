from django.contrib import admin

from .models import UserProfile
# from django.contrib.auth.models import User
# Register your models here.

@admin.register(UserProfile)
class AdminUserProfile(admin.ModelAdmin):
    # readonly_fields = ['dob']
    # list_display = ['username', 'first_name', 'last_name', 'email', 'mobile_no', 'address', 'dob', 'user_pic']
    list_display = ['mobile_no', 'address', 'dob', 'user_pic']
    list_filter = ('dob',)
    search_fields = ('dob',)


# here we create a custom user form

# from django.contrib.auth.admin import UserAdmin
# from .forms import CustomUserCreationForm, CustomUserChangeForm
# # from .models import CustomUser

# class CustomUserAdmin(UserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = UserProfile
#     list_display = ('mobile_no', 'address', 'dob', 'user_pic')
#     list_filter = ('dob',)
#     search_fields = ('dob',)
#     ordering = ('dob',)
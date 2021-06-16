from django.contrib import admin

# Register your models here.

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'address', 'phone', 'city', 'country']



admin.site.register(UserProfile, UserProfileAdmin)

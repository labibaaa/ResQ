from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'role', 'is_verified', 'is_active', 'date_joined']
    list_filter = ['role', 'is_verified', 'is_active']
    search_fields = ['username', 'email', 'nid_number']
    ordering = ['-date_joined']

    fieldsets = UserAdmin.fieldsets + (
        ('ResQ Profile', {
            'fields': ('role', 'nid_number', 'contact_number', 'occupation', 'workplace', 'date_of_birth', 'is_verified')
        }),
    )
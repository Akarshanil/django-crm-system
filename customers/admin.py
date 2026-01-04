from django.contrib import admin
from .models import Customer, UserProfile


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone', 'company', 'city', 'created_at']
    list_filter = ['created_at', 'city', 'state', 'country']
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'company']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('first_name', 'last_name', 'email', 'phone', 'image')
        }),
        ('Company Information', {
            'fields': ('company',)
        }),
        ('Address Information', {
            'fields': ('address', 'city', 'state', 'country', 'postal_code')
        }),
        ('Additional Information', {
            'fields': ('notes', 'created_by')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone']
    search_fields = ['user__username', 'user__email', 'phone']
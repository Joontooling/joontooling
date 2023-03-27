from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        *UserAdmin.fieldsets,  # original form fieldsets, expanded
        (                      # new fieldset added on to the bottom
            'userfield',  # group heading of your choice; set to None for a blank space instead of a header
            {
                'fields': (
                    'address',
                    'phone_number',
                    'user_type',
                    'company',
                    'per_company_number',
                    'company_number',
                    'point',
                    'like_products',
                ),
            },
        ),
    )

admin.site.register(User, CustomUserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Consumer


class CustomUserAdmin(UserAdmin):
    model = Consumer
    search_fields = ("email", "username", "first_name", "last_name")
    ordering = ("email",)
    fieldsets = (
        (
            None,
            {"fields": ("first_name", "last_name", "email", "username", "password",)},
        ),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "username",
                    "password",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )


admin.site.register(Consumer, CustomUserAdmin)

from django.contrib import admin
from main.models import *

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
        Model describing how to display info about users of web interface 
    """
    list_display = ("id", "username", "verified_usr")
    search_fields = ("id", "username")

    fieldsets = (

        ("Params", {
            "fields": ("username", "verified_usr", "is_superuser", "groups")

        }),
    )


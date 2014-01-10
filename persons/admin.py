# Django
from django.contrib import admin

# Local Apps
from core.admin import BaseModelAdmin
from .models import Person


class PersonAdmin(BaseModelAdmin):
    list_display = ['id', 'username', 'is_superuser', 'email', 'created']
    fieldsets = (
        ('Basic', {
            'fields': ('id', 'username', 'first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser',)
        }),
        ('Chronology', {
            'fields': ('last_login', 'created', 'modified')
        })
    )
    readonly_fields = ['id', 'is_superuser', 'last_login', 'created', 'modified']


admin.site.register(Person, PersonAdmin)

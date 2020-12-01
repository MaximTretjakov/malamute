from django.contrib import admin
from .models import CiUser


class CiUserAdmin(admin.ModelAdmin):
    list_display = ('avatar', 'username')
    ordering = ['username']


admin.site.register(CiUser, CiUserAdmin)

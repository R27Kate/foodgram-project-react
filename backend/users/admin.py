from django.contrib.admin import register
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Follow


@register(CustomUser)
class MyUserAdmin(UserAdmin):
    list_display = ('pk', 'username', 'email',
                    'first_name', 'last_name',
                    'is_staff', 'date_joined')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('username', 'email', 'first_name', 'last_name')
    empty_value_display = '-empty-'


@register(Follow)
class FollowAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'author')
    search_fields = ('user', 'author')
    list_filter = ('user', 'author')

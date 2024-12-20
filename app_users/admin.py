from django.contrib import admin
from django.contrib.auth.models import Group

from app_users.models import UserModel, Customer, Admin

admin.site.unregister(Group)
admin.site.register(Admin)


@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email']
    list_display_links = ['email']
    search_fields = ['full_name']
    save_on_top = True
    list_per_page = 3


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email']
    list_display_links = ['email']
    search_fields = ['full_name']
    save_on_top = True
    list_per_page = 3

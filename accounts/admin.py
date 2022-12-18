from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from .forms import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username','email','first_name','last_name','phone','is_staff', 'diamond']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'img', 'diamond')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('phone', 'img',)}),
    )



admin.site.register(User, CustomUserAdmin)
admin.site.register(Phone)
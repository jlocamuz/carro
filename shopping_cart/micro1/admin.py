from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from .models import *

admin.site.register(User)
admin.site.register(ClientDetail)
admin.site.register(ShoppingCart)
admin.site.register(CartDetail)
admin.site.register(Sale)
admin.site.register(SaleDetail)
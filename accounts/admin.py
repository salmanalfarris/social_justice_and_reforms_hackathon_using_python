from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Customer, Order
from .forms import CustomUserCreationForm, CustomUserChangeForm

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product_name', 'quantity', 'order_date')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')  # Example fields
    search_fields = ('name', 'email')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'customer', 'status', 'date_created')
    list_filter = ('status',)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['username', 'email', 'role', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'phone_number', 'address')}),
    )

admin.site.register(User, CustomUserAdmin)
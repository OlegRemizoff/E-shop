from django.contrib import admin
from .models import Order, OrderPhoneItem

# Register your models here.



class OrderPhoneItemInline(admin.TabularInline):
# Атрибут inlines позволяет вставлять мо-дель в ту же страницу редактирования,
#                                               что и связанная с ней модель
    model = OrderPhoneItem
    raw_id_fields = ['phone']

class OrderAdmin(admin.ModelAdmin):

    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address','city', 'paid','created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderPhoneItemInline]







admin.site.register(Order, OrderAdmin)
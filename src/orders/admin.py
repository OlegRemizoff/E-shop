from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.



class OrderItemInline(admin.TabularInline):
# Атрибут inlines позволяет вставлять мо-дель в ту же страницу редактирования,
#                                               что и связанная с ней модель
    model = OrderItem
    raw_id_fields = ['phone', 'note']

class OrderAdmin(admin.ModelAdmin):

    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address','city', 'paid','created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]








admin.site.register(Order, OrderAdmin)
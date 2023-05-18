from django.contrib import admin
from .models import Order, OrderPhoneItem, OrderNoteItem

# Register your models here.



class OrderPhoneItemInline(admin.TabularInline):
# Атрибут inlines позволяет вставлять мо-дель в ту же страницу редактирования,
#                                               что и связанная с ней модель
    model = OrderPhoneItem
    raw_id_fields = ['phone']
    verbose_name_plural = "Смартфоны"


class OrderNoteItemInline(admin.TabularInline):

    model = OrderNoteItem
    raw_id_fields = ['note']
    verbose_name_plural = "Ноутбуки"



class OrderAdmin(admin.ModelAdmin):

    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address','city', 'paid','created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderPhoneItemInline, OrderNoteItemInline]







admin.site.register(Order, OrderAdmin)
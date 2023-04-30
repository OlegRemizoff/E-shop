from django.contrib import admin
from django.utils.safestring import mark_safe
from django.forms import ModelChoiceField

from .models import Category, SmartPhone, Notebook


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug',)
    prepopulated_fields = {"slug": ("name",)}


class SmartPhoneAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price',
                    'show_image', 'available',)
    list_editable = ('available', )
    list_filter = ('available', 'price', )
    prepopulated_fields = {"slug": ("title",)}

    def show_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        else:
            return "None"

    show_image.__name__ = 'Миниатюра'

    # Ограничивает выбор категории
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class NotebookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price',
                    'show_image', 'available', )
    list_editable = ('available', )
    list_filter = ('available', 'price', )
    prepopulated_fields = {"slug": ("title",)}

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def show_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        else:
            return "None"

    show_image.__name__ = 'Миниатюра'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(SmartPhone, SmartPhoneAdmin)

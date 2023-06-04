from modeltranslation.translator import register, TranslationOptions
from .models import Category, SmartPhone, Notebook, Tv



@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(SmartPhone)
class SmartPhoneTranslationOptions(TranslationOptions):
    fields = ('color', 'description', 'camera', 'memory',)


@register(Notebook)
class NotebookTranslationOptions(TranslationOptions):
    fields = ('color', 'description', 'battery', )


@register(Tv)
class TvTranslationOptions(TranslationOptions):
    fields = ('color', 'description', )
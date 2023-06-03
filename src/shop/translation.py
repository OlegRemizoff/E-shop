from modeltranslation.translator import register, TranslationOptions
from .models import Category, SmartPhone, Notebook, Tv



@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


@register(SmartPhone)
class SmartPhoneTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(Notebook)
class NotebookTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )


@register(Tv)
class TvTranslationOptions(TranslationOptions):
    fields = ('title', 'description', )
from django import template
from shop.models import Category
register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


# Функция принимает текущий url адрес и обрасывает язык (/ru/ или /en/)
# результат будет подставлен в форму в виде href="/lang/{{ res }}" 
# чтобы при смене языка остаться на той же странице
@register.simple_tag()
def get_path_for_lang(path:str)->str:
    result = path[4:]
    return result

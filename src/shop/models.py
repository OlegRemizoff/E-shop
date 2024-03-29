from django.db import models
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType


class LatestProductsManager:

    @staticmethod
    def get_products_for_main_page(*args, **kwargs):
        products = []
        ct_models = ContentType.objects.filter(model__in=args)
        for ct_model in ct_models:
            model_products = ct_model.model_class(
            )._base_manager.all().select_related('category').order_by('id')[:3]
            products.extend(model_products)

        return products


class LatestProducts:

    objects = LatestProductsManager()


class Category(models.Model):
    '''Категория'''
    name = models.CharField("Имя категории", max_length=255)
    slug = models.SlugField("URL", unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_category', args=[self.id])


class Product(models.Model):
    '''Товар'''
    title = models.CharField("Наименование", max_length=255)
    slug = models.SlugField("URL", unique=True)
    brand = models.CharField("Фирма", max_length=255, null=True, blank=True)
    image = models.ImageField('Изображение', blank=True, upload_to='img/')
    price = models.FloatField('Цена', default=0.00)
    description = models.TextField('Описание', blank=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    available = models.BooleanField('Доступен', default=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория")
    color = models.CharField('Цвет', max_length=100)
    year = models.IntegerField('Год', blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.category.slug, self.slug])


class SmartPhone(Product):
    '''Смартфоны'''
    display = models.CharField('Экран', max_length=255, blank=True)
    memory = models.CharField('Память', max_length=255, blank=True)
    camera = models.CharField('Камера', max_length=255, blank=True)
    battery = models.CharField('Аккумулятор', max_length=255, blank=True)
    cpu = models.CharField('Процессор', max_length=255, blank=True)
    sim = models.CharField('SIM-карты', max_length=255, blank=True)
    os = models.CharField('Операционная система', max_length=255, blank=True)
    communication = models.CharField(
        'Стандарты связи', max_length=255, blank=True)
    weight = models.CharField('Вес', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Смартфон'
        verbose_name_plural = 'Смартфоны'

    def __str__(self) -> str:
        return f'{self.category.name} {self.title}'


class Notebook(Product):
    '''Ноутбуки'''
    os = models.CharField('Операционная система', max_length=255, blank=True)
    display = models.CharField('Экран', max_length=255, blank=True)
    graphic = models.CharField('Видеокарта', max_length=255, blank=True)
    memory = models.CharField('Память', max_length=255, blank=True)
    battery = models.CharField('Аккумулятор', max_length=255, blank=True)
    cpu = models.CharField('Процессор', max_length=255, blank=True)
    weight = models.CharField('Вес', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Ноутбук'
        verbose_name_plural = 'Ноутбуки'

    def __str__(self):
        return f'{self.category.name} {self.title}'


class Tv(Product):
    "Телевизоры"
    diagonal = models.CharField('Диагональ', max_length=255, blank=True)
    resolution = models.CharField('Разрешение', max_length=255, blank=True)
    display_type = models.CharField('Технология экрана', max_length=255, blank=True)
    frequency = models.CharField('Частота обновления', max_length=255, blank=True)
    brightness = models.CharField('Яркость', max_length=255, blank=True)
    interfaces = models.CharField('Разъёмы и нтерфейсы', max_length=255, blank=True)
    wireless =  models.CharField('Беспроводные интерфейсы', max_length=255, blank=True)
    smart_tv = models.CharField('Smart TV', max_length=255, blank=True)
    sound = models.CharField('Мощность звука', max_length=255, blank=True)

    class Meta:
        verbose_name = 'Телевизор'
        verbose_name_plural = 'Телевизоры'

    def __str__(self) -> str:
        return f'{self.category.name} {self.title}'
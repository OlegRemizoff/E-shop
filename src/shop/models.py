from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    '''Категория'''
    name = models.CharField("Имя категории", max_length=255)
    slug = models.SlugField("URL", unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.name


class Product(models.Model):
    '''Товар'''
    title = models.CharField("Наименование", max_length=255)
    slug = models.SlugField("URL", unique=True)
    image = models.ImageField('Изображение', blank=True, upload_to='img/')
    price = models.DecimalField(
        'Цена', max_digits=9, decimal_places=3, default=0.00)
    description = models.TextField('Описание', blank=True)
    digital = models.BooleanField(default=False, null=True, blank=True)
    available = models.BooleanField('Доступен', default=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Категория")

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.title


class SmartPhone(Product):
    '''Смартфоны'''
    os = models.CharField('Операционная система', max_length=255, blank=True)
    display = models.CharField('Экран', max_length=255, blank=True)
    camera = models.CharField('Камера', max_length=255, blank=True)
    memory = models.CharField('Память', max_length=255, blank=True)
    battery = models.CharField('Аккумулятор', max_length=255, blank=True)
    cpu = models.CharField('Процессор', max_length=255, blank=True)
    sim = models.CharField('SIM-карты', max_length=255, blank=True)
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

    def __str__(self) -> str:
        return f'{self.category.name} {self.title}'

from django.db import models
from shop.models import SmartPhone, Notebook, Tv



class Order(models.Model):

    first_name = models.CharField('Имя', max_length=50)
    last_name = models.CharField('Фамилия', max_length=50)
    email = models.EmailField()
    city = models.CharField('город', max_length=100)
    address = models.CharField('адрес', max_length=250)
    created = models.DateTimeField('Создан', auto_now_add=True)
    updated = models.DateTimeField('Обновлен', auto_now=True)
    paid = models.BooleanField('Оплачен', default=False)

    class Meta:
        ordering = ['-created']
        indexes = [models.Index(fields=['-created']), ]
        


class OrderItem(models.Model):
    
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    phone = models.ForeignKey(SmartPhone, related_name='order_phone',
                               on_delete=models.CASCADE, verbose_name="Телефон", blank=True, null=True)
    note = models.ForeignKey(Notebook, related_name='order_note',
                               on_delete=models.CASCADE, verbose_name="Ноутбук", blank=True, null=True)
    tv = models.ForeignKey(Tv, related_name='order_tv',
                               on_delete=models.CASCADE, verbose_name="Телевизор", blank=True, null=True)
    
    price = models.DecimalField(max_digits=10,  decimal_places=2, verbose_name="Цена")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Кол-во")
    
    def __str__(self):
        return str(self.id)
    



from django.db import models
from shop.models import SmartPhone, Notebook






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
        

class OrderPhoneItem(models.Model):
    
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    phone = models.ForeignKey(SmartPhone, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10,  decimal_places=3)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.id
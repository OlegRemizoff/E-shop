from django.shortcuts import render, redirect
from shop.models import SmartPhone, Notebook
import json

# Create your views here.


def index(request):
    cart = request.session.get('cart') # [{'type': 'Смартфоны', 'id': 3, 'qty': 1, slug: slug}, ]
    items = []
    TYPE_MODEL_CLASS = {
        'Смартфоны': SmartPhone,
        'Ноутбуки': Notebook,
    }

    if cart:
        # print("\x1b[31;1m" + 'CART' + "\x1b[0m", cart)
        for i in cart:
            current_model = TYPE_MODEL_CLASS[i['type']] # определяем текущую модель
            product = current_model._base_manager.get(id=i['id']) # получаем queryset

            # формируем словарь с нужными данными и добавляем его в список
            add_data = { 
                'id': product.id,
                'slug': product.slug,
                'title': product.title,
                'price': product.price,
                'qty': i['qty']

            }
            items.append(add_data) 
           # [{'id': 2, 'slug': 'google-pixel-7', 'title': 'Google Pixel 7', 'price': Decimal('59.990'), 'qty': 1}, ...]

    return render(request, 'cart/cart_detail.html', {'items': items})


def add_to_cart(request, type, id, slug, qty=1):
    if request.method == "POST":
        if not request.session.get('cart'):  # если нет корзины, то создаем ее
            request.session['cart'] = list()  # лист для хранения словарей
        else:
            # создаем список с предыдущими значен
            request.session['cart'] = list(request.session['cart'])

        # проверяем есть ли внутри списка, {} с такими значен.
        item_exists = next(
            (item for item in request.session['cart'] if item['type'] == type and item['id'] == id), False)

        if request.POST.get('quantity'):
            qty = request.POST.get('quantity')
        add_data = {
            'type': type,
            'id': id,
            'slug': slug,
            'qty': qty,
        }

        if not item_exists:
            request.session['cart'].append(add_data)
            request.session.modified = True

    return redirect(request.POST.get('url_from'))
    # return redirect('shop:home')


def remove_from_cart(request, slug):
    if request.method == "POST":

        # удаляем элемент из корзины
        for item in request.session['cart']:
            if item['slug'] == slug:
                item.clear()

        # удаляем  пустые {} из cart list()
        while {} in request.session['cart']:
            request.session['cart'].remove({})

        # удаляем cart list() из сессии
        if not request.session['cart']:
            del request.session['cart']
            # request.session.modified = True

        request.session.modified = True  # сохраняем изменения
    return redirect('cart:cart_detail')


def delete_cart(request):
    if request.session.get('cart'):
        del request.session['cart']

    return redirect('cart:cart_detail')









# from decimal import Decimal
# from django.conf import settings
# from shop.models import SmartPhone


# class Cart:

#     def __init__(self, request):
#         '''
#         Инициализация корзины
#         '''
#         self.session = request.session # сохранение текущего сеанса для других методов класса Cart
#         cart = self.session.get(settings.CART_SESSION_ID)
#         if not cart:
#             # сохраняем пустую каозину
#             cart = self.session[settings.CART_SESSION_ID] = {}
#         self.cart = cart

#     def add(self, product, quantity=1, override_quantity=False):
#         """
#         Добавить товар в корзину либо обновить его количество.
#         """
#         product_id = str(product.id)
#         if product_id not in self.cart:
#             self.cart[product_id] = {'quantity': 0,
#                                      'price': str(product.price)}
#         if override_quantity:
#             self.cart[product_id]['quantity'] = quantity
#         else:
#             self.cart[product_id]['quantity'] += quantity
#         self.save()

#     def remove(self, product):
#         """
#         Удалить товар из корзины
#         """
#         product_id = str(product.id)
#         if product_id in self.cart:
#             del self.cart[product_id]
#             self.save()


#     def save(self):
#         # пометить сеанс как "измененный",
#         # чтобы обеспечить его сохранение
#         self.session.modified = True

#     def __iter__(self):
#         """"
#         Прокрутить товарные позиции корзины в цикле и
#         получить товары из базы данных.
#         """
#         product_ids = self.cart.keys() # получаем все экземпляры класса Product(SmartPhone)
#         products = SmartPhone.objects.filter(id__in=product_ids)
#         cart = self.cart.copy() # Текущая корзина копируется в переменную cart

#         for product in products:
#             cart[str(product.id)]['product'] = product # и в нее добавляются экземпляры класса Product
#         for item in cart.values():
#             item['price'] = Decimal(item['price']) # Конвертируем цену каждого товара
#             item['total_price'] = item['price'] * item['quantity'] # +аттрибут total в каждый товар
#             yield item

#     def __len__(self):
#         """
#         Подсчитать все товары в корзине
#         """
#         return sum(item['quantity'] for item in self.cart.values()) # values() - возвращает ключи

#     def get_total_price(self):
#         return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

#     def clear(self):
#         # удалить корзину из сеанса
#         del self.session[settings.CART_SESSION_ID]
#         self.save()

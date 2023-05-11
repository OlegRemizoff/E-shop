from django.shortcuts import render, redirect
from shop.models import SmartPhone, Notebook

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
            
            if request.POST.get('quantity'):
                qty = request.POST.get('quantity')
                add_data = { 
                    'id': product.id,
                    'slug': product.slug,
                    'title': product.title,
                    'price': product.price,
                    'qty': qty,

                }
            else:
                # формируем словарь с нужными данными и добавляем его в список
                add_data = { 
                    'id': product.id,
                    'slug': product.slug,
                    'title': product.title,
                    'price': product.price,
                    'qty': i['qty'],

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


def change_quantity(request, slug):
    if request.method == 'POST':
        for item in request.session['cart']:
            if item['slug'] == slug:
                item['qty'] = request.POST.get('quantity')
                request.session.modified = True
    return redirect('cart:cart_detail')


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









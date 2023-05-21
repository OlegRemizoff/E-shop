from django.shortcuts import render, redirect
from shop.models import SmartPhone, Notebook, Tv


# Create your views here.


def cart(request):
    cart = request.session.get('cart') # [{'type': 'Смартфоны', 'id': 3, 'qty': 1, slug: slug}, ]
    items = []
    total_price = 0

    TYPE_MODEL_CLASS = {
        'Смартфоны': SmartPhone,
        'Ноутбуки': Notebook,
        'Телевизоры': Tv,
    }

    if cart:
        # print("\x1b[31;1m" + 'CART' + "\x1b[0m", cart)
        for i in cart:
            current_model = TYPE_MODEL_CLASS[i['type']] # определяем текущую модель
            product = current_model._base_manager.get(id=i['id']) # получаем queryset
            product_sum = i['product_sum']
            
            if product_sum == 0:
                product_sum = product.price

            # qty = i['qty']
            if request.POST.get('quantity'):
                qty = request.POST.get('quantity')

                # формируем словарь с нужными данными и добавляем его в список
                add_data = { 
                    'id': product.id,
                    'slug': product.slug,
                    'title': product.title,
                    'image': product.image,
                    'color': product.color,
                    'price': product.price,
                    'qty': qty,
                    'product_sum': product_sum

                }
            else:
                    add_data = { 
                    'id': product.id,
                    'slug': product.slug,
                    'title': product.title,
                    'image': product.image,
                    'color': product.color,
                    'price': product.price,
                    'qty': i['qty'],
                    'product_sum': product_sum

                }

            items.append(add_data) 
           # [{'id': 2, 'slug': 'google-pixel-7', 'title': 'Google Pixel 7', 'price': Decimal('59.990'), 'qty': 1}, ...]
        for i in items:
            total_price += float(i['product_sum'])       

    return render(request, 'cart/cart_detail.html', {'items': items, 'total_price': total_price})


def add_to_cart(request, type, id, slug, qty=1, product_sum=0):
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
            qty = request.POST.get('quantity') # Кол-во из формы detail.html
        add_data = {
            'type': type,
            'id': id,
            'slug': slug,
            'qty': qty,
            'product_sum': product_sum,
        }

        if not item_exists:
            request.session['cart'].append(add_data)
            request.session.modified = True

    return redirect(request.POST.get('url_from'))


def change_quantity(request, slug):

    def get_float(string):
        res = string[:-2]
        return float(res)

    if request.method == 'POST':
        # получаем данные из формы обновления товара
        str_price = request.POST.get('price')
        price = get_float(str_price)
        print(str_price)
        print(price)
        qty = request.POST.get('quantity')
  
        for item in request.session['cart']:
            if item['slug'] == slug:
                item['qty'] = qty
                item['product_sum'] = str(price * int(qty))
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












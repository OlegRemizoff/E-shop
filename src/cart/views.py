from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    cart = request.session.get('cart')
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def add_to_cart(request, type, id):
    if request.method == "POST":
        if not request.session.get('cart'): # если нет корзины, то создаем ее
            request.session['cart'] = list() # лист для хранения словарей
        else:
            request.session['cart'] = list(request.session['cart']) # создаем список с предыдущими значен


        # item_exists = next((item for item in request.session['cart'] if item['id'] == id), False)

        item_exists = next((item for item in request.session['cart'] if item['type'] == request.POST.get('type') and item['id'] == id), False)

        add_data = {
            # 'type': request.POST.get('type'),
            'type': type,
            'id': id,    
        }

        if not item_exists:
            request.session['cart'].append(add_data)
            request.session.modified = True
    return redirect('shop:home')


def remove_from_cart(request, id):
    if request.method == "POST":

        # удаляем элемент из корзины
        for item in request.session['cart']:
            if item['type'] == request.POST.get('type') and item.id == id:
                item.clear()

        # удаляем  пустые {} из cart list()
        while {} in request.session['cart']:
            request.session['cart'].remove({})


        # удаляем cart list() из сессии
        if not request.session['cart']:
            del request.session['cart']
            # request.session.modified = True 

        request.session.modified = True # сохраняем изменения
    return redirect('shop:home')

def delete_cart(request):
    if request.session.get('cart'):
        del request.session['cart']
    # return redirect(request.POST.get('url_from'))
    return redirect('cart:cart_detail')
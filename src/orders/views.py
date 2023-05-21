from django.shortcuts import render, redirect
from django.contrib import messages
from shop.models import SmartPhone, Notebook, Tv
from .models import  OrderItem
from .forms import OrderCreateForm



# Create your views here.


def order_create(request):
    pass

    cart = request.session.get('cart') # [{'type': 'Смартфоны', 'id': 3, 'qty': 1, slug: slug}, ]
    items = []  # для корзины
    query = {}  # для заказа
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

            qty = i['qty']
            if request.POST.get('quantity'):
                qty = request.POST.get('quantity')


            query[product] = qty


            # словарь для корзины
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


            items.append(add_data) 

        for i in items:
            total_price += float(i['product_sum']) 
 

        order_items = query.items()
        # for item in order_items:
        #     product = item[0]
        #     qty = item[1]
        #     print("\x1b[31;1m" + 'product' + "\x1b[0m", product.price * Decimal(qty))

       
    ### форма заказа ###
    form = OrderCreateForm(request.POST)
    if form.is_valid():
        order = form.save()
        for item in order_items:
            product = item[0]
            qty = int(item[1])
            if product.category.id == 1:
                OrderItem.objects.create(order=order,
                                    note=product,
                                    quantity=qty,
                                    price=product.price * qty)
                
            elif product.category.id == 2:
                OrderItem.objects.create(order=order,
                                    phone=product,
                                    quantity=qty,
                                    price=product.price * qty)
                
            elif product.category.id == 3:
                OrderItem.objects.create(order=order,
                                    tv=product,
                                    quantity=qty,
                                    price=product.price * qty)
            
                
        del request.session['cart']      
        messages.success(request, 'Оплата завершена !')      
        return redirect('cart:cart_detail')

    else:
        form = OrderCreateForm()
        return render(request, 'orders/create.html', {'form': form,
                                                        'items': items,
                                                        'total_price': total_price})


    


























# print("\x1b[31;1m" + 'Type' + "\x1b[0m", type(item.category.id))




  




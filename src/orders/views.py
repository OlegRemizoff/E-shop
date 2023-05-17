from django.shortcuts import render
from shop.models import SmartPhone, Notebook
from .models import Order, OrderPhoneItem
from .forms import OrderCreateForm


# Create your views here.


def order_create(request):
    cart = request.session.get('cart')
    items = []
    total_price = 0
    query = []

    TYPE_MODEL_CLASS = {
        'Смартфоны': SmartPhone,
        'Ноутбуки': Notebook,
    }
    if cart:

        for i in cart:
            current_model = TYPE_MODEL_CLASS[i['type']] 
            product = current_model._base_manager.get(id=i['id']) 
            product_sum = i['product_sum']
            
            query.append(product)

            if product_sum == 0:
                product_sum = product.price

            qty = i['qty']
            if request.POST.get('quantity'):
                qty = request.POST.get('quantity')

            add_data = { 
                'id': product.id,
                'slug': product.slug,
                'title': product.title,
                'image': product.image,
                'price': product.price,
                'qty': qty,
                'product_sum': product_sum

            }


            items.append(add_data) 
            # [{'id': 2, 'slug': 'google-pixel-7', 'title': 'Google Pixel 7', 'price': Decimal('59.990'), 'qty': 1}, ...]

        for i in items:
            total_price += float(i['product_sum']) 


            ### форма заказа ###
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                for item in query:
                    OrderPhoneItem.objects.create(order=order,
                                         phone=item,
                                         quantity=qty,
                                         price=item.price)
                return render(request, 'orders/create.html', {'order': order, 'form': form})

        else:
            form = OrderCreateForm()
            return render(request, 'orders/create.html', {'form': form})








# <class 'shop.models.SmartPhone'>

            # if request.method == 'POST':
            #     form = OrderCreateForm(request.POST)
            #     if form.is_valid():
            #         order = form.save()
            #         for item in product:
            #             OrderItem.objects.create(order=order,
            #                                  product=item['note'])
            #         return render(request, 'orders/create.html', {'order': order})

            #     else:
            #         form = OrderCreateForm()
            #         return render(request, 'orders/create.html', {'form': form})

        

















        #     query.append(product)
        #     print("\x1b[31;1m" + 'Query' + "\x1b[0m", query)

        #     if product_sum == 0:
        #         product_sum = product.price

        #     qty = i['qty']
        #     if request.POST.get('quantity'):
        #         qty = request.POST.get('quantity')

        #     add_data = { 
        #         'id': product.id,
        #         'slug': product.slug,
        #         'title': product.title,
        #         'image': product.image,
        #         'price': product.price,
        #         'qty': qty,
        #         'product_sum': product_sum

        #     }


        #     items.append(add_data) 
        #     # [{'id': 2, 'slug': 'google-pixel-7', 'title': 'Google Pixel 7', 'price': Decimal('59.990'), 'qty': 1}, ...]

        # for i in items:
        #     total_price += float(i['product_sum'])    


        ### Форма заказа ###   
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                for item in query:
                    OrderItem.objects.create(order=order,
                                             product=item['note'])
                return render(request, 'orders/create.html', {'order': order})
    # Query [<SmartPhone: Смартфоны Xiaomi POCO X4 Pro 5G 8>, <SmartPhone: Смартфоны Google Pixel 7>]
        else:
            form = OrderCreateForm()

        return render(request, 'orders/create.html', {'form': form})




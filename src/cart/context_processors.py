

def cart(request):
    cart = request.session.get('cart')
    url_array = [] # если slug в корзине будет == item.slug вкл нужные include.html c иконками корзины 
    if cart != None:
        product_count = len(cart)
        for i in cart: 
            url_array.append(i['slug'])
        
    else:
        product_count = 0
    return {'product_count': product_count,'url_array': url_array}




def cart(request):
    cart = request.session.get('cart')
    if cart != None:
        product_count = len(cart)
    else:
        product_count = 0
    return {'product_count': product_count}
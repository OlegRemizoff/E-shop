from django.urls import path
from .views import cart, add_to_cart, remove_from_cart, change_quantity, add_to_cart_ajax




app_name = "cart"

urlpatterns = [
    path('', cart, name="cart_detail"),
    path('cart_add/', add_to_cart_ajax, name='ajax_cart'),
    path('<str:type>/<int:id>/<str:slug>/', add_to_cart, name="add"),
    path('<str:slug>/', remove_from_cart, name="remove"),
    path('update/<str:slug>/', change_quantity, name='change_quantity'),

    
]
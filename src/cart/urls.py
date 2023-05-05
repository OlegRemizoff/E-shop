from django.urls import path
from .views import index, add_to_cart, remove_from_cart, delete_cart




app_name = "cart"

urlpatterns = [
    path('', index, name="cart_detail"),
    path('<str:type>/<int:id>/add/', add_to_cart, name="add"),
    path('<str:type>/<int:id>/remove/', remove_from_cart, name="remove"),
    path('delete/', delete_cart, name="delete"),

    
]
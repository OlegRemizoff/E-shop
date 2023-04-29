from django.shortcuts import render
from django.views.generic import View

from .models import LatestProducts


# Create your views here.


class HomeView(View):
    
    def get(self, request, *args, **kwargs):
        products = LatestProducts.objects.get_products_for_main_page(
            "smartphone", "notebook")
        return render(request, 'shop/index.html', {"products": products})
from django.shortcuts import render, get_list_or_404
from django.views.generic import View, DeleteView

from .models import LatestProducts,  Category, Notebook, SmartPhone


# Create your views here.


class HomeView(View):
    
    def get(self, request, *args, **kwargs):
        products = LatestProducts.objects.get_products_for_main_page(
            "smartphone", "notebook")
        return render(request, 'shop/index.html', {"products": products})
    

class ProductDetailView(DeleteView):

    MODEL_MODEL_CLASS = {
        "notebooks": Notebook,
        "smartphones": SmartPhone,
    }

    def dispatch(self, request, *args, **kwargs):
        # забираем имя модели из **kwargs (urls/path(<str:ct_model>) ) и оределяем имя модели
        self.model = self.MODEL_MODEL_CLASS[kwargs['model_name']]
        self.queryset = self.model._base_manager.all()
        return super().dispatch(request, *args, **kwargs)
    
    # model = Model
    # queryset = Models.objects.all()
    context_object_name = "product"
    template_name = 'shop/detail.html'
    slug_url_kwarg = 'slug'



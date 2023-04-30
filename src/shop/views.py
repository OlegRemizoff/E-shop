from django.shortcuts import render
from django.views.generic import View, DetailView

from .models import LatestProducts, Notebook, SmartPhone


# Create your views here.


class HomeView(View):

    def get(self, request, *args, **kwargs):
        products = LatestProducts.objects.get_products_for_main_page(
            "smartphone", "notebook")
        return render(request, 'shop/index.html', {"products": products})


class ProductDetailView(DetailView):

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


class ProductByCategoryView(View):

    CATEGORY_MODEL_CLASS = {
        1: Notebook,
        2: SmartPhone,

    }

    def get(self, request, *args, **kwargs):
        # pk = kwargs.get('id')
        category_model = self.CATEGORY_MODEL_CLASS[kwargs['pk']]
        category = category_model._base_manager.all()
        return render(request, 'shop/category_list.html', {'category': category})

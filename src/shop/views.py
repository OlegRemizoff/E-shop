from django.shortcuts import render
from django.views.generic import View, DetailView, TemplateView
from django.core.paginator import Paginator
import random

from .models import LatestProducts, Notebook, SmartPhone, Tv


# Create your views here.


class HomeView(View):

    def get(self, request, *args, **kwargs):
        products = LatestProducts.objects.get_products_for_main_page(
            "smartphone", "notebook", 'tv')
        random.shuffle(products)
        return render(request, 'shop/index.html', {"products": products})


class ProductDetailView(DetailView):

    MODEL_MODEL_CLASS = {
        "notebooks": Notebook,
        "smartphones": SmartPhone,
        "televizory": Tv,
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
        3: Tv,

    }

    def get(self, request, *args, **kwargs):
        # pk = kwargs.get('id')
        category_model = self.CATEGORY_MODEL_CLASS[kwargs['pk']]
        category = category_model._base_manager.all()

        paginator = Paginator(category, 6)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        return render(request, 'shop/category_list.html', {'page_obj': page_obj, 'category': category})


class Search(TemplateView):
    template_name = 'shop/search.html'
    products = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        phone = SmartPhone.objects.filter(title__icontains=self.request.GET.get('s'))
        note = Notebook.objects.filter(title__icontains=self.request.GET.get('s'))

        self.products.clear()
        self.products.extend(note) 
        self.products.extend(phone) 

        context['products'] = self.products
        return context








    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['phone'] = SmartPhone.objects.filter(title__icontains=self.request.GET.get('s'))
    #     context['note'] = Notebook.objects.filter(title__icontains=self.request.GET.get('s'))
    #     # context['s'] = f"s={self.request.GET.get('s')}&" # для пагинации
    #     return context






from django.shortcuts import render
from django.views.generic import View, DetailView, TemplateView
from django.core.paginator import Paginator
import random

from .models import LatestProducts, Notebook, SmartPhone, Tv
from .utils import CategoryBrandCount


# Create your views here.

CATEGORY_MODEL_CLASS = {

    1: Notebook,
    2: SmartPhone,
    3: Tv,

}


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


class ProductByCategoryView(CategoryBrandCount, View):

    def get(self, request, *args, **kwargs):
        # pk = kwargs.get('id')
        category_model = CATEGORY_MODEL_CLASS[kwargs['pk']]

        # Кол-во товаров определенного бренда для сайдбара
        brand_count = CategoryBrandCount.get_brand_count(self, category_model)

        ### Order ###
        if request.GET.get('res'):
            category = category_model._base_manager.select_related('category').order_by(
                request.GET.get('res'))
        else:
            category = category_model._base_manager.select_related('category').order_by('id')

        ### Show ###
        if request.GET.get('show'):
            paginator = Paginator(category, request.GET.get('show'))
        else:
            paginator = Paginator(category, 6)

        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        res_sort = f"res={request.GET.get('res', '')}&"  # для пагинации

        return render(request, 'shop/category_list.html', {'page_obj': page_obj,
                                                           'category': category,
                                                           'brand_count': brand_count,
                                                           'res_sort': res_sort, })


class Search(TemplateView):
    template_name = 'shop/search.html'
    products = []

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        phone = SmartPhone.objects.filter(
            title__icontains=self.request.GET.get('s'))
        note = Notebook.objects.filter(
            title__icontains=self.request.GET.get('s'))
        tv = Tv.objects.filter(title__icontains=self.request.GET.get('s'))

        self.products.clear()
        self.products.extend(note)
        self.products.extend(phone)
        self.products.extend(tv)

        context['products'] = self.products
        return context


class CategoryFilterView(View):

    def get(self, request, *args, **kwargs):

        category_model = CATEGORY_MODEL_CLASS[kwargs['pk']]
        category = category_model._base_manager.all()

        # Кол-во товаров определенного бренда для сайдбара
        brand_count = CategoryBrandCount.get_brand_count(self, category_model)
        other = CategoryBrandCount.get_other_brand(self, category_model)
        print(other)

        # Получение и возвращение результата фильтрации

        def get_queryset():
            kwargs = {}
            if request.GET.getlist('brand'):
                kwargs['brand__in'] = request.GET.getlist('brand')
            if request.GET.getlist('year'):
                kwargs['year__in'] = request.GET.getlist('year')

            # queryset = category_model._base_manager.filter(
            #     Q(year__in=selected_years) &

            #     Q(brand__in=selected_values)

            #     )

            return category_model._base_manager.filter(**kwargs).prefetch_related()
        
        queryset = None
        if request.GET.get('other'):
            queryset = other
        else:
            queryset = get_queryset()



        paginator = Paginator(queryset, 6)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)

        return render(request, 'shop/filter.html', {'page_obj': page_obj,
                                                    "category": category,
                                                    'brand_count': brand_count})

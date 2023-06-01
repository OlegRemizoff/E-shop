from django.db.models import Q


class CategoryBrandCount:

    def get_brand_count(self, category_model):
        brand_count = {}
        brands = ['apple', 'samsung', 'sony', 'xiaomi', 'huawei', ]

        apple = len(category_model._base_manager.filter(brand__icontains='apple'))
        samsung = len(category_model._base_manager.filter(brand__icontains='samsung'))
        sony = len(category_model._base_manager.filter(brand__icontains='sony'))
        xiaomi = len(category_model._base_manager.filter(brand__icontains='xiaomi'))
        huawei = len(category_model._base_manager.filter(brand__icontains='huawei'))
        other = len(category_model._base_manager.filter(~Q(brand__in=brands)))


        brand_count['apple'] = apple
        brand_count['samsung'] = samsung
        brand_count['sony'] = sony
        brand_count['xiaomi'] = xiaomi
        brand_count['huawei'] = huawei
        brand_count['other'] = other
        return brand_count
    
    def get_other_brand(self, category_model):
        brands = ['apple', 'samsung', 'sony', 'xiaomi', 'huawei', ]
        other = category_model._base_manager.filter(~Q(brand__in=brands))
        return other
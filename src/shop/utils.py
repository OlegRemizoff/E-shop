
class CategoryBrandCount:

    def get_brand_count(self, category_model):
        brand_count = {}
        apple = len(category_model._base_manager.filter(brand__icontains='apple'))
        samsung = len(category_model._base_manager.filter(brand__icontains='samsung'))
        sony = len(category_model._base_manager.filter(brand__icontains='sony'))
        xiaomi = len(category_model._base_manager.filter(brand__icontains='xiaomi'))
        huawei = len(category_model._base_manager.filter(brand__icontains='huawei'))

        brand_count['apple'] = apple
        brand_count['samsung'] = samsung
        brand_count['sony'] = sony
        brand_count['xiaomi'] = xiaomi
        brand_count['huawei'] = huawei
        return brand_count
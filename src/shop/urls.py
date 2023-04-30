from django.urls import path
from .views import HomeView, ProductDetailView,  ProductByCategoryView


app_name = "shop"

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('products/<str:model_name>/<str:slug>/', ProductDetailView.as_view(), name="product_detail"),
    path("category/<int:pk>/", ProductByCategoryView.as_view(), name='product_category'),
    
]
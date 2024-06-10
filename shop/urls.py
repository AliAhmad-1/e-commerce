from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

app_name='shop'

# path('shop/products/<slug:category_slug>/',views.products_list,name='products_list_by_category'),

urlpatterns = [
    path('',views.home,name='home'),
    path('shop/products/',views.products_list,name='products_list'),
    path('shop/product/<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
]

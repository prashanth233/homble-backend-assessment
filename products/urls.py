from django.urls import path
from . import views

from .views import products_list, update_sku_status

urlpatterns = [
    path('products/', views.products_list, name='products_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('skus/create/', views.create_sku, name='create_sku'),
    path('sku/<int:pk>/update-status/', update_sku_status, name='update_sku_status'),

]

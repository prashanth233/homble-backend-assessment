from django.urls import path
from .views import CategoryProductListView

urlpatterns = [
    path('categories/', CategoryProductListView.as_view(), name='category-product-list'),
]

from django.urls import path

from.views import test_view, ProductDetailView, CartView, AddToCartView

urlpatterns = [
    path('', test_view, name='base'),
    path('products/<str:ct_model>/<str:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('cart/', CartView.as_view(), name='cart'),
    path('add-to-cart/<str:ct_model>/<str:slug>/', AddToCartView.as_view(), name='add_to_cart')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('learn/', views.learn, name='learn'),
    path('products/', views.products_index, name='index'),
    path('products/<int:product_id>/', views.products_detail, name='detail'),
    path('accounts/signup/', views.signup, name='signup'),
    path('cart/', views.cart, name='cart'),
    path('products/<int:product_id>/add/',
         views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),


]

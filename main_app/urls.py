from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import remove_from_cart


urlpatterns = [
    path('', views.home, name='home'),
    path('logout', views.logout_view),
    path('learn/', views.learn, name='learn'),
    path('products/', views.products_index, name='index'),
    path('products/<int:product_id>/', views.products_detail, name='detail'),
    path('products/<int:product_id>/add_review/',
         views.add_review, name='add_review'),
    # path('products/<int:product_id>/reviews/edit/', views.edit_review, name="edit_review"),
    path('products/<int:product_id>/reviews/delete/',
         views.delete_review, name="delete_review"),
    path('accounts/signup/', views.signup, name='signup'),
    path('cart/', views.cart, name='cart'),
    path('products/<int:product_id>/add/',
         views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('cart/<int:product_id>/remove/',
         views.remove_from_cart, name='remove-from-cart'),
    path('cart/<int:product_id>/update/',
         views.update_cart, name='update-cart'),
    path('create-checkout-session/', views.CreateCheckoutSessionView.as_view(),
         name='create-checkout-session'),
    path('success/', views.checkout_success, name='checkout_success'),
    path('cancel/', views.checkout_cancel, name='checkout_cancel'),
    path('account/', views.account_view, name='account'),
    path('order/<int:order_id>/', views.order_detail_view, name='order_detail'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

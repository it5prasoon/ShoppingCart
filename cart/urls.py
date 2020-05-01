from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<int:product_id>/', views.RemoveOne, name='RemoveOne'),
    path('full_remove/<int:product_id>/', views.RemoveAll, name='RemoveAll'),
]
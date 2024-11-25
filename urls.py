from django.urls import path

from . import views

app_name = 'work'

urlpatterns = [
    path('', views.choose, name="choose"),
    path('sell/', views.sell, name="sell"),
    path('buy/', views.buy, name="buy"),
    path('buy/<int:pk>/', views.item, name="item"),
    path('buy/<int:pk>/cart/', views.cart_item, name="cart_item"),
    path('buy/before_cart/<int:pk>/', views.before_cart, name='before_cart'),
    path('buy/cart/', views.cart, name='cart'),
    path('sell/add_item/', views.add_item, name='add_item')
]
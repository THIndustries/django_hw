from django.urls import path
from . import views
from .views import get_orders, ProductsListCreateView

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('orders/<int:user>/<int:days>', show_orders, name='show_orders'),
    path('user/<int:user_id>/orders_for_last/<int:days>/', views.get_orders),
    path('products/', views.ProductsListCreateView.as_view(), name='products')
]
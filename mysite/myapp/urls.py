from django.urls import path
from . import views
from .views import show_orders

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('orders/<int:user>/<int:days>', show_orders, name='show_orders')
]
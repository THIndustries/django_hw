from django.shortcuts import render
from django.http import HttpResponse
import logging
from .models import Order, Product
from datetime import timedelta, timezone
from django.utils.timezone import now
from django.db.models import F, Sum
from .models import OrderProduct
from django.views.generic.edit import CreateView
from .forms import ProductForm

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Главная страница посещена')
    return render(request, 'home.html')

def about(request):
    logger.info('Страница обо мне посещена')
    return render(request, 'about.html')


def get_orders(request, days, user_id):
    date = timezone.now() - timezone.timedelta(days=days)
    result = OrderProduct.objects.prefetch_related('order', 'product').filter(
        order__created_at__gt=date, order__customer=user_id
    ).values(
        name=F('product__name')
    ).annotate(
        count=Sum('order_amount')
    )
    context = {
        'days': days,
        'products': result,
    }

    return render(request, 'homeworkapp/products_by_date.html', context)


# Homework 4
class ProductsListCreateView(CreateView):
    model = Product
    template_name = 'homeworkapp/products.html'
    form_class = ProductForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = self.model.objects.all()
        return context
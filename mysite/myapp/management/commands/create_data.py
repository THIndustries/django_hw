from django.core.management.base import BaseCommand
from myapp.models import Order, Client, OrderProduct, Product
from faker import Faker
from random import randint, choice, uniform

fake = Faker('ru_RU')


class Command(BaseCommand):
    help = "Generate fake data for User "
    PRODUCTS = [
        'Картофель', 'Морковь', 'Лук', 'Чеснок', 'Петрушка', 'Укроп', 'Яблоки', 'Бананы', 'Лимон',
        'Масло сливочное', 'Кефир', 'Молоко', 'Сметана', 'Творог', 'Сыр',
        'Горчица', 'Малиновое варенье', 'Томатная паста', 'Рыбная консерва', 'Консервированный горошек',
        'Консервированная кукуруза', 'Сгущенка', 'Мед',
    ]
    ORDERS_PER_PERSON = 3
    PRODUCTS_PER_ORDER = 5
    MAX_PRODUCTS_IN_ORDER = 5
    PRODUCTS_AMOUNT = 100

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='Amount of fake data')

    def handle(self, *args, **options):
        count = options['count']
        users = []
        for _ in range(count):
            user = Client(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.unique.phone_number().replace(' ', '').replace('(', '').replace(')', '').replace('-',
                                                                                                                   ''),
                address=fake.address(),
            )
            user.save()
            users.append(user)

        products = []
        for p in self.PRODUCTS:
            product = Product(
                name=p,
                description=p,
                price=round(uniform(50, 300), 2),
                amount=self.PRODUCTS_AMOUNT,
            )
            product.save()
            products.append(product)

        for user in users:
            for _ in range(self.ORDERS_PER_PERSON):
                order = Order(
                    customer=user,
                    created_at=fake.date_time_between('-1y'),
                )
                order.save()
                products_copy = products.copy()
                for _ in range(self.PRODUCTS_PER_ORDER):
                    random_product = choice(products_copy)
                    products_copy.remove(random_product)
                    OrderProduct(
                        order=order,
                        product=random_product,
                        order_amount=randint(1, self.MAX_PRODUCTS_IN_ORDER),
                    ).save()
                order.save()
        self.stdout.write(
            self.style.SUCCESS(f"Fake data created!")
        )
from django.core.management.base import BaseCommand
from myapp.models import Client

class Command(BaseCommand):
    help = 'Creates a new client'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone_number', type=str)
        parser.add_argument('address', type=str)

    def handle(self, *args, **options):
        Client.objects.create(
            name=options['name'],
            email=options['email'],
            phone_number=options['phone_number'],
            address=options['address']
        )
        self.stdout.write(self.style.SUCCESS(f'Successfully created client: {options["name"]}'))

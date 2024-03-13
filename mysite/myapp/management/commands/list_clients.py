from django.core.management.base import BaseCommand
from myapp.models import Client

class Command(BaseCommand):
    help = 'Lists all clients'

    def handle(self, *args, **options):
        for client in Client.objects.all():
            self.stdout.write(f'{client.id}: {client.name}, {client.email}, {client.phone_number}, {client.address}, Registered: {client.registration_date}')

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from listings.models import Listing
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed the database with sample Listings'

    def handle(self, *args, **kwargs):
        # Create a host user if none exists
        host, _ = User.objects.get_or_create(username='hostuser', defaults={'email': 'host@example.com', 'password': 'password'})

        for i in range(10):
            Listing.objects.create(
                title=f'Sample Listing {i+1}',
                description='A lovely place to stay.',
                location=random.choice(['Lagos', 'Abuja', 'Accra', 'Nairobi']),
                price_per_night=random.randint(50, 200),
                host=host
            )
        self.stdout.write(self.style.SUCCESS('Database seeded with sample listings.'))

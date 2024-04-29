from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a superuser'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'password')
            self.stdout.write(self.style.SUCCESS('Successfully created a new superuser'))
        else:
            self.stdout.write(self.style.WARNING('Admin user already exists.'))

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):
    help = "A simple test command that create test user."

    def handle(self, *args, **options):
        username = "testuser"
        password = "test"
        email = "test@test.com"
        try:
            user_obj = User.objects.create(username=username, email=email)
            user_obj.set_password(password)
            user_obj.save()
            self.stdout.write('Successfully created test user')
        except:
            print("Error Occurred")


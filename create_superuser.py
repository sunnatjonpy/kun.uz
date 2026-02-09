import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from accounts.models import CustomUser

# Superuser ma’lumotlari
EMAIL = os.environ.get('SUPERUSER_EMAIL', 'webpython9@gmail.com')
USERNAME = os.environ.get('SUPERUSER_USERNAME', 'admin')
PASSWORD = os.environ.get('SUPERUSER_PASSWORD', 'python 4307')

if not CustomUser.objects.filter(email=EMAIL).exists():
    CustomUser.objects.create_superuser(
        username=USERNAME,
        email=EMAIL,
        password=PASSWORD
    )
    print("✅ Superuser created")
else:
    print("⚠️ Superuser already exists")

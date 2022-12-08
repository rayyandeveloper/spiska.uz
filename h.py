import sys
sys.dont_write_bytecode = True

# Django specific settings
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()


from home.models import Category, Shop


for i in Shop.objects.all():
    for x in range(1, 16, 1):
        Category.objects.create(name=f"{x}-kategoriya", shop=i)
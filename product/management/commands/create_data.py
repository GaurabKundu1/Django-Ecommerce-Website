import requests
from django.utils.text import slugify
from django.core.management.base import BaseCommand
from product.models import Category, Product

class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Creating data...")
        response = requests.get('https://fakestoreapi.com/products').json()

        for product in response:
            category, _ = Category.objects.get_or_create(
                title=product['category'],
                slug=slugify(product['category']),
                featured=True
            )

            # Check if the product already exists
            existing_product = Product.objects.filter(title=product['title']).first()

            if existing_product:
                # Update existing product or handle as needed
                existing_product.price = product['price']
                existing_product.thumbnail = product['image']
                existing_product.description = product['description']
                existing_product.save()
            else:
                Product.objects.create(
                    category=category,
                    title=product['title'],
                    slug=slugify(product['title']),
                    price=product['price'],
                    thumbnail=product['image'],
                    description=product['description'],
                )

        print("Insertion complete!")

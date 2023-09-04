"""
It is like of creating the fixtures but using out database
The way we use the models to create the form here we use it to
create the factory, we add the data which we need.

Later from here in the conftest we register these factories and there we create
fixtures and prepare our models either use build or create.

Then in our test cases we use them and check all the conditions
"""

import factory
from django.contrib.auth import get_user_model
from faker import Faker
from app1 import models
fake = Faker()

User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = fake.name()
    is_staff = True

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = "Nike"

class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    title = "Runnin shoes"
    category = factory.SubFactory(CategoryFactory)
    description = fake.text()
    slug = "Running-shoes"
    regular_price = 9.99
    discount_price = 4.99

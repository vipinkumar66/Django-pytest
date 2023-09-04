"""
In the conftest we basically adds our fixtures that runs before all the tests
"""

import pytest
from pytest_factoryboy import register
from tests.factories import UserFactory, CategoryFactory, ProductFactory

register(UserFactory)
register(CategoryFactory)
register(ProductFactory)


"""Creating the user but not saving it to database and
sending it to the test
"""
# @pytest.fixture
# def create_user(db, user_factory):
#     user = user_factory.build()
#     return user


@pytest.fixture
def create_product(db, product_factory):
    product = product_factory.build()
    return product

# @pytest.fixture()
# def create_user_fixture(db):
#     user_ = User.objects.create(username="Vipin",
#                         email="vipin@vipin.com")
#     user_.set_password("vipin")
#     return user_

# @pytest.fixture()
# def create_user_fixture(db):
#     def create_user(
#         username:str = "username",
#         password:str = None,
#         first_name: str = "firstname",
#         last_name:str = "lastname",
#         email:str = "email@email.com",
#         is_staff: str = False,
#         is_active: str = True,
#         is_superuser: str = False
#     ):
#         user_ = User.objects.create(username=username, password=password,
#                         first_name=first_name, last_name=last_name,
#                         email=email, is_staff=is_staff, is_active=is_active,
#                         is_superuser=is_superuser)
#         return user_
#     return create_user

# @pytest.fixture
# def create_normal_user(db, create_user_fixture):
#     return create_user_fixture("Vipin", "vipin", "Djangodeveloper")

# @pytest.fixture
# def create_super_user(db, create_user_fixture):
#     return create_user_fixture("Vipin", "vipin", "Djangodeveloper", is_superuser=True)
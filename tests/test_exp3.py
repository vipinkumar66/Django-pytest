import pytest
from django.contrib.auth import get_user_model

User = get_user_model()

# @pytest.fixture
# def create_user(db):
#     return User.objects.create_user("vipin")


# @pytest.mark.django_db
# def test_check_user(create_user):
#     create_user.set_password("vipin")
#     assert create_user.check_password("vipin") is True


# def test_user_password(create_normal_user):
#     print(create_normal_user.username)
#     assert create_normal_user.is_superuser is False

# def test_superuser_password(create_super_user):
#     print(create_super_user.username)
#     assert create_super_user.is_superuser is True

"""This is how we use the data from the factories and here
we are creating the user and checking it.
But there is one more method in which we can create the user in the
factory and then return it and we can use it here
Shown in the next function
"""
# @pytest.mark.django_db
# def test_superuser_password(user_factory):
#     # This will create the user for us
#     # user = user_factory.build()
#     user = user_factory.create() #will add him to the database also and for that
#     # we need a database
#     print(user.username)
#     assert User.objects.all().count() == 1


# @pytest.mark.django_db
# def test_superuser_password(user_factory):
#     print(user_factory.username)


@pytest.mark.django_db
def test_create_product(create_product):
    print(create_product.description)
    assert True
import pytest


# @pytest.fixture
# def create_user(db):
#     return User.objects.create_user("vipin")


# @pytest.mark.django_db
# def test_check_user(create_user):
#     create_user.set_password("vipin")
#     assert create_user.check_password("vipin") is True


def test_user_password(create_normal_user):
    print(create_normal_user.username)
    assert create_normal_user.is_superuser is False

def test_superuser_password(create_super_user):
    print(create_super_user.username)
    assert create_super_user.is_superuser is True


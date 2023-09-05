import pytest
from app1.models import Product
from factories import CategoryFactory

@pytest.mark.parametrize(
    "title,category, description, slug, regular_price, discount_price, validity",
    [
        ("title1",1, "Description1", "slug",
        "9.99", "3.99", True),
        ("title2", 1,"Description2", "slug",
        "9.99", "3.99", True)
    ]
)
def test_create_product(
    db, product_factory, title,category, description, slug,
    regular_price, discount_price, validity,
):
    # category_instance = CategoryFactory()
    test = product_factory(
        title = title,
        category_id = category,
        description = description,
        slug = slug,
        regular_price = regular_price,
        discount_price = discount_price,
    )
    item = Product.objects.all().count()
    assert validity == item
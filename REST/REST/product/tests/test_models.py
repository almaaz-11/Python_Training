import pytest
from product.models import Product

@pytest.mark.django_db
def test_product_creation():
    product = Product.objects.create(
        name="Laptop",
        price=50000,
        stock=10,
        description="Gaming laptop",
        is_active=True
    )

    assert product.id is not None
    assert product.name == "Laptop"
    assert product.stock == 10
    assert product.is_active is True

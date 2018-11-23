import pytest

from admitad.gateway import Item


@pytest.fixture(scope="module")
def item():
    return Item(internal_id=1, item_price=100, quantity=5)


def test_item_internal_id(item):
    assert item.internal_id == 1


def test_item_price(item):
    assert item.price == 100


def test_item_quantity(item):
    assert item.quantity == 5

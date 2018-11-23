import pytest

from admitad.gateway import Item, Order


@pytest.fixture(scope="module")
def item():
    return Item(internal_id=1, item_price=100, quantity=5)


@pytest.fixture(scope="module")
def order():
    return Order(internal_id=1, postback_key='postback_key', items=[Item(1, 100, 5)])


def test_add_item(order, item):
    assert order.add_item(item)
    assert item in order.items


def test_order_items(order, item):
    for order_item in order.items:
        assert item.__eq__(order_item)


def test_full_price(order):
    assert order.full_price == 1000

def test_items_count(order):
    assert order.items_count == 2
# django-admitad
[![Build Status](https://travis-ci.org/Picasel/django-admitad.svg?branch=master)](https://travis-ci.org/Picasel/django-admitad)
[![codecov](https://codecov.io/gh/Picasel/django-admitad/branch/master/graph/badge.svg)](https://codecov.io/gh/Picasel/django-admitad)
[![Python versions](https://img.shields.io/pypi/pyversions/django-admitad.svg)](https://pypi.python.org/pypi/django-admitad)
[![Pypi](https://img.shields.io/pypi/v/django-admitad.svg)](https://pypi.python.org/pypi/django-admitad)

Django reusable app for integration with Admitad CPA via postback requests

## Requirements

* [Python 3.7](https://www.python.org/downloads/release/python-370/)
* [Django 2.1.3](https://www.djangoproject.com/)

## Installation
```sh
$ pip install django-admitad
```

## Configuration
To enable django-admitad for your project you need to add `admitad` to `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'admitad'
]
```

You also need to configure some Admitad CPA settings:
```python
ADMITAD_COMPAIN_CODE = 'example_compain'
ADMITAD_POSTBACK_URL = 'https://ad.admitad.com/r'
ADMITAD_POSTBACK_KEY = 'example_postback_key'
```

Don't forget to run migrations:
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

## Usage
To send a postback requests, you need to create an `Order` and `Item` objects:
```python
from admitad.gateway import Order, Item

item = Item(internal_id=1, item_price=100, tariff_code=1, quantity=2)
order = Order(internal_id=1, admitad_uid='12345', action_code=1)
```
And add `Item` objects to `Order`:
```python
order.add_item(item)
```
Items can also be directly transferred to the order:
```python
items = [Item(internal_id=1, item_price=100, tariff_code=1, quantity=2)]
order = Order(internal_id=1, admitad_uid='12345', action_code=1, items=items)
```
And finally send postback requests
```python
order.send_postback_requests()
```
All sent requests and parameters are saved to the database and are accessible from the admin
![test](https://pp.userapi.com/c847017/v847017946/135ac6/7i7AL8Y_DFE.jpg)


## TODO
 * Celery integration
 * Integration tests & test coverage (>90%)
 * Support for old versions of Python/Django
 
## License
MIT

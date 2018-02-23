from decimal import Decimal
from django.conf import settings
from products.models import Item, Specs


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, specs_id):
        if specs_id not in self.cart:
            self.cart[specs_id] = {'quantity': 1}
        else:
            self.cart[specs_id]['quantity'] += 1
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, specs_id):
        if specs_id in self.cart:
            del self.cart[specs_id]
            self.save()

    def __getitem__(self, key):
        return self.cart[key]

    def __iter__(self):
        for item in self.cart.keys():
            yield item

    def cart_len(self):
        return len([item for item in self.cart])

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True

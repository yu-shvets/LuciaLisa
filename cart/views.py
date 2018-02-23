from django.shortcuts import render, HttpResponseRedirect, reverse
from cart.cart import Cart
from products.models import Specs
from django.contrib import messages


def cart_view(request):
    cart_items = []
    cart = Cart(request)
    for item in cart:
        specs = Specs.objects.get(id=int(item))
        quantity = cart[item]['quantity']
        cart_items.append({'specs': specs, 'quantity': quantity, 'total_price': specs.price * quantity})
    cart_total = sum([item['total_price'] for item in cart_items])
    return render(request, 'cart/cart.html', {'cart_items': cart_items, 'cart_total': cart_total})


def add_cart(request):
    specs_id = request.POST.get('size_id', False)
    cart = Cart(request)
    cart.add(specs_id)
    messages.success(request, 'The item was successfully added to cart')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def cart_remove(request, specs_id):
    cart = Cart(request)
    cart.remove(specs_id)
    return HttpResponseRedirect(reverse('cart'))

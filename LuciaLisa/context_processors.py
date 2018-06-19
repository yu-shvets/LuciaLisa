from cart.cart import Cart


def project_variables(request):
    cart_length = Cart(request).cart_len()
    page_items = [4, 12, 24, 48]
    return {'cart_length': cart_length, 'page_items': page_items}

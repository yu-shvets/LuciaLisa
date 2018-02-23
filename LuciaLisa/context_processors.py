from cart.cart import Cart


def project_variables(request):
    cart_length = Cart(request).cart_len()
    return {'cart_length': cart_length}

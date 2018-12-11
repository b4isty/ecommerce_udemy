from django.shortcuts import render, redirect
from .models import Cart, Product
from orders.models import Order


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    # products = cart_obj.products.all()
    return render(request, 'carts/home.html', {'cart': cart_obj})


def cart_update(request):
    product_id = request.POST.get("product_id")
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, Product is gone")
            return redirect('cart:home')
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        request.session['cart_items'] = cart_obj.products.count()
    return redirect('cart:home')


def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    order_obj = None
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:home")
    order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    return render(request, "carts/checkout.html", {"object": order_obj})

# def checkout_home(request):
#     cart_obj, cart_created = Cart.objects.new_or_get(request)
#     if cart_created or cart_obj.products.count() == 0:
#         return redirect("cart:home")
#     try:
#         order_obj = Order.objects.get(cart=cart_obj)
#     except Order.DoesNotExist:
#         order_obj = Order.objects.create(cart=cart_obj)
#     return render(request, "carts/checkout.html", {"object": order_obj})

# def cart_home(request):
#     # print(request.session)
#     # print(dir(request.session))
#     key = request.session.session_key
#     print(key)
#     request.session['cart_id'] = 12  # set
#     # request.session['first_name'] = "Baishakhi"
#     # print(request.set_expiry(300))  # 5 minutes
#     # print(request.set_expiry)
#     return render(request, 'carts/home.html', {})


# def cart_create(user=None):
#     cart_obj = Cart.objects.create(user=None)
#     print("New cart created")
#     return cart_obj

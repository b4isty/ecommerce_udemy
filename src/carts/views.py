from django.shortcuts import render, redirect
from .models import Cart, Product
from orders.models import Order
from accounts.forms import LoginForm, GuestForm
from billing.models import BillingProfile
from accounts.models import GuestEmail


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
    # order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    billing_profile = None
    login_form = LoginForm()
    guest_form = GuestForm()
    guest_email_id = request.session.get("guest_email_id")
    if request.user.is_authenticated():
        billing_profile, billing_profile_created = BillingProfile.objects.get_or_create(user=request.user,
                                                                                        email=request.user.email)
    elif guest_email_id is not None:
        guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
        billing_profile, billing_guest_profile_created = BillingProfile.objects.get_or_create(
            email=guest_email_obj.email)
    else:
        pass

    if billing_profile is not None:
        order_qs = Order.objects.filter(billing_profile=billing_profile, cart=cart_obj, active=True)
        if order_qs.count() == 1:
            order_obj = order_qs.first()
        else:
            print("----------------", billing_profile, cart_obj)
            old_order_qs = Order.objects.exclude(billing_profile=billing_profile).filter(cart=cart_obj)
            print(old_order_qs)
            if old_order_qs.exists():
                old_order_qs.update(active=False)
            order_obj = Order.objects.create(billing_profile=billing_profile, cart=cart_obj)
            print("order_created", order_obj)

    # if billing_profile is not None:
    #     order_qs = Order.objects.filter(cart=cart_obj, active=True)
    #     if order_qs.exists():
    #         order_qs.update(active=False)
    #     else:
    #         order_obj = Order.objects.create(billing_profile=billing_profile, cart=cart_obj)

    context = {
        "object": order_obj,
        "billing_profile": billing_profile,
        "login_form": login_form,
        "guest_form": guest_form
    }

    return render(request, "carts/checkout.html", context)

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

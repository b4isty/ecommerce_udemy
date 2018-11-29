from django.shortcuts import render
from .models import Cart


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    print(products)
    total = 0
    for x in products:
        total += x.price
    print(total)

    return render(request, 'carts/home.html', {})

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

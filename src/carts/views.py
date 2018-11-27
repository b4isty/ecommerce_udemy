from django.shortcuts import render


def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    # print(cart_id)
    if cart_id is None:  # and isinstance(cart_id, int)
        print("Create new cart")
        request.session["cart_id"] = 0
    else:
        print("Cart Id exists")
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

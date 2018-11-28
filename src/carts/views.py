from django.shortcuts import render
from .models import Cart


def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    qs = Cart.objects.filter(id=cart_id)
    if qs.count() == 1:
        print("Cart Id exists")
        cart_obj = qs.first()
        if request.user.is_authenticated() and cart_obj.user is None:
            cart_obj.user = request.user
            cart_obj.save()
    else:
        cart_obj = Cart.objects.new(user=request.user)
        request.session['cart_id'] = cart_obj.id
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

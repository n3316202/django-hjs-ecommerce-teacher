from django.shortcuts import render
from cart.cart import Cart

# Create your views here.


# dev_15
def add_cart(request):
    cart = Cart(request)

    print("카트======", cart)

    if request.POST.get("action") == "post":

        # 상품 받아오기
        product_id = int(request.POST.get("product_id"))
        print("product_id", product_id)

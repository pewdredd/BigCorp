from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .cart import Cart
from shop.models import ProductProxy


def cart_view(request):
    cart = Cart(request)
    context = {'cart': cart}
    return render(request, 'cart/cart-view.html', context=context)

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':

        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        product = get_object_or_404(ProductProxy, pk=product_id)

        cart.add(product=product, quantity=product_qty)

        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()

        responce = JsonResponse({'qty': cart_qty, 'total_price': cart_total})
        print('I add to cart')
        return responce

def cart_update(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))

        cart.update(product_id=product_id, quantity=product_qty)

        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()

        responce = JsonResponse({'qty': cart_qty, 'total_price': cart_total})

        return responce

def cart_delete(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        cart.delete(product_id=product_id)

        cart_qty = cart.__len__()
        cart_total = cart.get_total_price()

        responce = JsonResponse({'qty': cart_qty, 'total_price': cart_total})

        return responce

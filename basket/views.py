from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from .basket import Basket
from shop.models import Product
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages




def basket_summary(request):
    if request.user.is_authenticated:
        return render(request, 'shop/basket/summary.html')
    else:
        messages.info(request, 'please register or login to your account')
        return redirect('mainpage:home')


def basket_add(request):
    basket= Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid')) 
        product_qty = int(request.POST.get('productqty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, qty=product_qty)
        basketqty = basket.__len__()
        response = JsonResponse({'qty':basketqty})
        return response

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        basket.delete(product=product_id)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('productid'))
        product_qty = int(request.POST.get('productqty'))
        basket.update(product=product_id, qty=product_qty)

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({'qty': basketqty, 'subtotal': baskettotal})
        return response
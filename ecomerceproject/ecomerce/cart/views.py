from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect, get_object_or_404
from ecomerceA.models import product
from .models import cart,cartitem

# Create your views here.
def _cart_id(request):
    cartt=request.session.session_key
    if not cartt:
        cartt=request.session.create()
    return cartt


def add_cart(request,pproduct_id):
    pproduct=product.objects.get(id=pproduct_id)
    try:
        cartt=cart.objects.get(Cart_id=_cart_id(request))
    except cart.DoesNotExist:
        cartt=cart.objects.create(
                 Cart_id=_cart_id(request)
        )
        cartt.save()
    try:
        cartt_item=cartitem.objects.get(Product=pproduct,Cart=cartt)
        if cartt_item.quantity < cartt_item.Product.stock:
            cartt_item.quantity += 1
        cartt_item.save()
    except cartitem.DoesNotExist:
        cartt_item=cartitem.objects.create(
            Product=pproduct,
            quantity=1,
            Cart=cartt

        )
        cartt_item.save()
    return redirect('cart:cart_detail')
def cart_detail(request,total=0,counter=0,cart_items=None):
    try:

        cartt=cart.objects.get(Cart_id=_cart_id(request))
        cart_items=cartitem.objects.filter(Cart=cartt,active=True)
        for cart_item in cart_items:
            total += (cart_item.Product.price * cart_item.quantity)
            counter += cart_item.quantity

    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(cart_items=cart_items,total=total,counter=counter))

def cart_remove(request,pproduct_id):
    cartt=cart.objects.get(Cart_id=_cart_id(request))
    pproduct=get_object_or_404(product,id=pproduct_id)
    cart_item=cartitem.objects.get(Product=pproduct,Cart=cartt)
    if cart_item.quantity >1:
        cart_item.quantity -=1

        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')
def full_remove(request,pproduct_id):
    cartt=cart.objects.get(Cart_id=_cart_id(request))
    pproduct=get_object_or_404(product,id=pproduct_id)
    cart_item=cartitem.objects.get(Product=pproduct,Cart=cartt)
    cart_item.delete()
    return redirect('cart:cart_detail')

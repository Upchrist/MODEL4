from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from home.models import Setting
from product.models import *
from user.models import UserProfile
from django.contrib.auth.decorators import login_required
import requests
import json
import string
import uuid
from django.views.decorators.http import require_POST

# Create your views here.


def index(request):
    return HttpResponse('order app')

@require_POST
@login_required(login_url='/login')
def addtoshopcart(request):
    url = request.META.get('HTTP_REFERER')
    thequantity = int(request.POST['quantity'])
    thesize = request.POST.get['size',None]
    theprodid = request.POST['prodid']
    aprod = Product.objects.get(pk=theprodid)

    # check if the user has an existing cart
    cart = ShopCart.objects.filter(order_placed=False).filter(user__username = request.user.username)

    if cart: #an existing cart is noticed
    productchecker = ShopCart.objects.filter(product_id = aprod.id, size=thesize,
    quanity=thequantity,user__username = request.user.username).first()

    if productchecker: #product exist
        

    else: #product is not in the cart, add it
        anitem = ShopCart()
        anitem.product=aprod
        anitem.user=request.user
        anitem.order_code=cart[0].order_code
        anitem.quanity=thequantity
        anitem.size= thesize
        anitem.order_placed=False
        anitem.save()


    else: #create a new cart, generate order code
        ordercode = str(uuid.uuid4())
        newcart = ShopCart()
        newcart.product=aprod
        newcart.user=request.user
        newcart.order_code=ordercode
        newcart.quantity=thequantity
        newcart.size=thesize
        newcart



@login_required(login_url='/login')
def shopcart(request):
    category = Category.objects.all()
    setting= Setting.objects.get(pk=1)
    shopcart = shopcart.objects.filter(order_placed=False).filter(user__username=request.user.username)

    subtotal=0
    shippingfee= 0
    vat =0
    total = 0

    for item in shopcart:
        if item.product.discount_price:
            subtotal += item.product.discount_price * item.quantity
        else:
            subtotal += item.product.price * item.quantity

    # Shipping rules: 8% fees to all orders above 150. 0 fees to orders lower

    if subtotal > 150:
        shippingfee = 0.08 * subtotal
    else:
        shippingfee = 0

    vat = 0..075 * subtotal

    total = subtotal + shippingfee + vat

    context = {
        'setting': setting,
        'category': category,
        'shopcart': shopcart,
        'subtotal': subtotal,
        'shipping': shippingfee,
        'vat': vat,
        'total': total,
    }

    return render(request, 'shopcart.html', context)

@require_POST
@login_required(login_url='/login')
def updatequantity(request):
    url = request.META.get('HTTP_REFERER')
    newquantity = request.POST['itemquantity']
    theitem = ShopCart.objects.get(id=request.POST['itemid'])
    theitem.quantity = newquantity
    theitem.save()

    messages.success(request, "Product Quantity successfully updated")
    return redirect(url)


@login_required(login_url='/login')
def deletefromcart(request,id):
    ShopCart.objects.filter(id=id).delete()
    messages.success(request, 'item deleted from shopcart')
    return redirect('order:shopcart')

@login_required(login_url='/login')
def checkout(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    shopcart = ShiopCart.objects.filter(user__username = request.username).filter(order_placed=False)
    profile= UserProfile.objects.get(user__username =request.user.username)


    subtotal=0
    shippingfee = 0
    vat = 0
    total = 0

    for  item in shopcart:
        if item.product.discount_price:
            subtotal += item.product.discount_price * item.quantity
        else:
            subtotal += item.product.price * item.quantity
    
    # Shipping rules: 8% fees to all orders above 150. 0 fees to orders lower

    if subtotal > 150:
        shipping = 0.08 * subtotal
    else:
        shippingfee 0 

    # vat is at 7.50% of the total purchase to be made

    vat = 0.075 * subtotal

    total = subtotal + shippingfee + vat

    context ={
        'setting': setting,
        'shopcart': shopcart,
        'order_code': shopcart[0].order_code,
        'profile': profile,
        'category': category,
        'subtotal': subtotal,
        'ahipping': shippingfee,
        'vat': vat,
        'total': total,
    }

return render(request, 'checkout.html', context)

        



        

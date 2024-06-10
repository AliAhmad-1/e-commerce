from django.shortcuts import render,get_object_or_404,redirect
from shop.models import Product
from django.views.decorators.http import require_POST
from .cart import Cart
from .forms import CartAddProductForm
from django.http import JsonResponse
from coupons.forms import CouponApplyForm


# @require_POST
# def cart_add(request,product_id):
#     cart=Cart(request)
#     product=get_object_or_404(Product,id=product_id)
#     form=CartAddProductForm(request.POST)
#     if form.is_valid():
#         quantity=form.cleaned_data.get('quantity')
#         override=form.cleaned_data.get('override')
#         cart.add(product=product,quantity=quantity,override_quantity=override)
        
#     return redirect('cart:cart_detail')

@require_POST
def cart_add(request):
    
    cart=Cart(request)
    product_id=request.POST.get('product_id')
    product=get_object_or_404(Product,id=product_id)
    form=CartAddProductForm(request.POST)
    if form.is_valid():
        quantity=form.cleaned_data['quantity']
        override=form.cleaned_data.get('override')
        
        cart.add(product=product,quantity=quantity,override_quantity=override)

    cart_json=cart.serialize()
    return JsonResponse({'status':'OK','cart':cart_json})









# @require_POST
# def cart_remove(request,product_id):
#     cart=Cart(request)
#     product=get_object_or_404(Product,id=product_id)

#     cart.remove(product=product)
#     return redirect('cart:cart_detail')


@require_POST
def cart_remove(request):
    product_id=request.POST.get('product_id')
    cart=Cart(request)
    product=get_object_or_404(Product,id=product_id)

    cart.remove(product=product)
    cart=cart.serialize()
    return JsonResponse({'status':'Ok','cart':cart})

def cart_detail(request):
    cart=Cart(request)
    for item in cart:
        item['update_quantity_form']=CartAddProductForm(initial={
        'quantity':item['quantity'],
        'override':True
        })
    form=CouponApplyForm()
    return render(request,'cart_detail.html',{'form':form,'cart':cart})





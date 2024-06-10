from django.shortcuts import render,get_object_or_404
from .models import Product,Category
from cart.forms import CartAddProductForm
from .serializers import ProductSerializer
from django.http import JsonResponse
from .recommender import Recommender
# from cart.cart import Cart
# Create your views here.


# def products_list(request,category_slug=None):
#     category=None
#     categories=Category.objects.all()
#     products=Product.objects.filter(available=True)
#     if category_slug:
#         category=get_object_or_404(Category,slug=category_slug)
#         products=products.filter(category=category)

#     return render(request,'home.html',{'products':products,'category':category,'categories':categories})
def home(request):
    categories=Category.objects.all()
    products=Product.objects.filter(available=True)
 

    return render(request,'home.html',{'products':products,'categories':categories})

def products_list(request):
    category_slug=request.GET.get('category_slug')
    category=None
    categories=Category.objects.all()
    products=Product.objects.filter(available=True)
    if category_slug:
        category=get_object_or_404(Category,slug=category_slug)
        products=products.filter(category=category)
    
        category_json={'id':category.id,'name':category.name,'slug':category.slug}
        products_json=ProductSerializer(products,many=True)
     
        return JsonResponse({'status':'OK','products':products_json.data,'category':category_json})

    products_json=ProductSerializer(products,many=True)
    return JsonResponse({'status':'OK','products':products_json.data,'category':'All Products'})



def product_detail(request,id,slug):
    product=get_object_or_404(Product,id=id,slug=slug,available=True)
    form=CartAddProductForm()
    r=Recommender()
    recommended_products=r.suggest_products_for([product],4)
    
    return render(request,'product_detail.html',{'product':product,'form':form,'recomended_products':recommended_products})

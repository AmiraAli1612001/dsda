from django.shortcuts import render , redirect ,get_object_or_404
from django.http import Http404 
from .models import Product
from .models import SelectedProducts
def Home(request):
    products = Product.objects.all()
    return render(request ,"index.html" , {"products" : products})

def cart(request):
    cartProducts = SelectedProducts.objects.all()
    totalPrice = 0
    for product in cartProducts:
        totalPrice += product.totalPrice
    return render(request, "cart.html" , {"cartProdcuts" : cartProducts  , "totalPrice" : totalPrice})



def deleteProductFromCart(request , id):
    product = SelectedProducts.objects.get(id=id)
    product.delete()
    return redirect("products:cart")

def addToCart(request , id):
    product = Product.objects.get(id = id)
    SelectedProducts.objects.create(id = id , image = product.image , name=product.name , price = product.price , totalPrice = product.price * 1 , qty = 1 )
    return redirect("products:cart")


def product_details(request , id) :
    products = Product.objects.all()
    try:
        product = Product.objects.get(id = id)
    except:
        raise Http404("product not found")
    return render(request , "productDetails.html" ,{"products" : products  , "product" : product} )
from django.urls import path 
from . import views
app_name = "products"

urlpatterns = [

    path("home/" , views.Home , name="index") , 
    path("cart/" , views.cart , name="cart"),
    path("<int:id>/" ,  views.product_details , name="product_details"),
    path("delete/<int:id>/" ,  views.deleteProductFromCart , name="delete_product"),
    path("add/<int:id>/" ,  views.addToCart , name="add_product"),



    
]
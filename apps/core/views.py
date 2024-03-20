from django.shortcuts import render

# Create your views here.
from apps.product.models import Product

def frontpage(request):
    newest_products = Product.objects.all()[0:8]
    
    print("Newest Products",newest_products)
    return render(request,'core/frontpage.html',{'newest_products':newest_products})
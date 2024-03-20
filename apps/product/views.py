from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
# Create your views here.

import random

from .forms import AddToCartForm

from .models import Category, Product
from apps.cart.cart import Cart

def product_details(request,category_slug, product_slug):
    #cart
    cart = Cart(request)
    
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug )
    print('product from db::::', product)
    
    if request.method == "POST":
        form = AddToCartForm(request.POST)
        print("request.POST:::",request.POST)
        if form.is_valid():
            print("Form is valid?::",form.is_valid())
            quantity = form.cleaned_data['quantity']
            
            print("Form Quantity?::",quantity)
            cart.add(product_id=product.id, quantity=quantity, update_quantity=False)
            messages.success(request, "The product was added to Cart!")
            
            return redirect('product_details',category_slug=category_slug,product_slug=product_slug)
    else:
        form = AddToCartForm()
            
    similar_products = list(product.category.products.exclude(id=product.id))
    
    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products,4)
    return render(request, 'product/product_details.html',{'form':form,'product':product,'similar_products':similar_products,})

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    print("category_slug",category_slug,"category:::",category)
    return render(request, 'product/category.html',{"category":category})
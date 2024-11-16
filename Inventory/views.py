from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url=('/'))
def Productadd(request):
    context ={
        'Product_form' : ProductForm()
    }
    
    if request.method == 'POST':
        product_form = ProductForm(request.POST,request.FILES)
        if product_form.is_valid():
            product_form.save()
            
    return render (request,'products_add.html',context)

@login_required(login_url=('/'))
def Productlist(request):
    context={
        'all_products':Products.objects.all()
    }
    return render (request,'products.html',context)

@login_required(login_url=('/'))
def Productdelete(request,id):
    selected_products = Products.objects.get(id = id)
    selected_products.delete()
    return redirect ('/inventory/products/')

@login_required(login_url=('/'))
def Productupdate(request,id):
    selected_product = Products.objects.get(id=id)
    context ={
        'Product_form' : ProductForm(instance=selected_product)
    }
    if request.method == 'POST':
        product_form = ProductForm(request.POST,instance=selected_product)
        if product_form.is_valid():
            product_form.save()
            return redirect('/inventory/products/')
    
    return render (request,'products_add.html',context)




    


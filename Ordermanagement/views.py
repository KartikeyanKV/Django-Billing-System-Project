from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def Customeradd(request):
    context = {
        'customer_form' : CustomerForm()
    }
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('/ordermanagement/customers/')
            
    return render(request,'Customers_add.html',context) 

@login_required(login_url='/')
def Customerlist(request):
    context={
        'all_customers':Customer.objects.all()
    }
    return render (request,'customers.html',context)

@login_required(login_url='/')
def Customerdelete(request,id):
    selected_customers = Customer.objects.get(id = id)
    selected_customers.delete()
    return redirect ('/ordermanagement/customers/')

@login_required(login_url='/')
def Customerupdate(request,id):
    selected_customers = Customer.objects.get(id=id)
    context ={
        'customer_form' : CustomerForm(instance=selected_customers)
    }
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST,instance=selected_customers)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('/ordermanagement/customers/')
    
    return render (request,'customers_add.html',context)

@login_required(login_url='/')
def Orderadd(request):
    context ={
        'order_form' : OrderForm()
    }
    
    if request.method == 'POST':
        selected_product = Products.objects.get(id = request.POST['Product_reference'])
        amount = float(selected_product.product_price)*float(request.POST['quantity'])
        gst = (amount * selected_product.product_GST)/100
        bill_amount = amount * gst
        
        
        new_order = Order(Product_reference_id = request.POST['Product_reference'],customer_reference_id = request.POST['customer_reference'],
        order_date = request.POST['order_date'],quantity = request.POST['quantity'],amount=amount,gst = gst,bill_amount = bill_amount,
        order_number = request.POST['order_number'])
        new_order.save()
            
    return render (request,'orders_add.html',context)

@login_required(login_url='/')
def Orderlist(request):
    context={
        'all_orders':Order.objects.all()
    }
    return render (request,'orders.html',context)

@login_required(login_url='/')
def Orderdelete(request,id):
    order = Order.objects.get(id = id)
    order.delete()
    return redirect ('/ordermanagement/orders/')

@login_required(login_url='/')
def Orderupdate(request,id):
    order =  Order.objects.get(id = id)
    context ={
        'order_form' : OrderForm(instance= order)
    }
    if request.method =='POST':
        selected_product = Products.objects.get(id = request.POST['Product_reference'])
        amount = float(selected_product.product_price)*float(request.POST['quantity'])
        gst = (amount * selected_product.product_GST)/100
        bill_amount = amount * gst
        
        order_filter = Order.objects.filter(id = id)
        order_filter.update(Product_reference_id = request.POST['Product_reference'],customer_reference_id = request.POST['customer_reference'],
        order_date = request.POST['order_date'],quantity = request.POST['quantity'],amount=amount,gst = gst,bill_amount = bill_amount,
        order_number = request.POST['order_number'])
        return redirect ('/ordermanagement/orders/')
        
    return render (request,'orders_add.html',context)    
        

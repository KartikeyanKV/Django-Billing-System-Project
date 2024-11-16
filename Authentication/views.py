from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth import authenticate,login,logout


def Loginpage(request):
    
    if request.user.is_authenticated:
        return redirect('/inventory/products/')
    context = {
       'error':'' 
    }
    if request.method == "POST":
        
        user = authenticate(username = request.POST['username'],password = request.POST['password'])
        
        if user is not None:
            
            login (request,user)
            
            return redirect('/inventory/products/')
        
        else:
            context = {
                'error':'*Invalid Username or Password'
            }
            return render (request,'login.html',context)
    
    return render (request,'login.html')

def Logout(request):
    logout(request)
    return redirect('/')

def Signup(request):
    context = {
        'error':''
    }
    if request.method =='POST':
        check_user = User.objects.filter(username = request.POST['username'])
        print (check_user)
        
        if len(check_user) >0:
            context = {
                'error':'*Username already Taken'
            }
            return render (request,'signup.html',context)
        
        else:
        
            new_user = User(username = request.POST['username'],first_name = request.POST['first_name'],last_name = request.POST['last_name'],
            email = request.POST['email'],age = request.POST['age'],role = request.POST['role'])
            new_user.set_password(request.POST['password'])
            
            new_user.save()
            return redirect('/')
        
    return render (request,'signup.html',context)

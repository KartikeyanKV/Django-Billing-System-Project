from django.urls import path
from .views import *

urlpatterns = [
    
    path('customers/add/',Customeradd),
    path('customers/',Customerlist),
    path('customers/delete/<int:id>/',Customerdelete,name='customerdelete'),
    path('customers/update/<int:id>/',Customerupdate,name='customerupdate'),
    
    
    path('orders/add/',Orderadd),
    path('orders/',Orderlist),
    path('orders/delete/<int:id>/',Orderdelete,name='orderdelete'),
    path('orders/update/<int:id>/',Orderupdate,name='orderupdate'),
    
]

from django.urls import path
from .views import *

urlpatterns=[
    path('products/add/',Productadd),
    path('products/',Productlist),
    path('product/delete/<int:id>/',Productdelete,name='productdelete'),
    path('product/update/<int:id>/',Productupdate,name= 'productupdate'),
]
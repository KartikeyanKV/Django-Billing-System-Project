from django.urls import path
from .views import *

urlpatterns= [
    
    path ('',Loginpage),
    path ('logout/',Logout),
    path('signup/',Signup)
]

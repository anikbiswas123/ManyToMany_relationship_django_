from django.urls import path
from .views import *

urlpatterns = [
    
    path('',home,name='home'),
    path('AboutUs/',AboutUs,name='AboutUs'),
    # customer
    path('add_customer/',add_customer,name='add_customer'),
    path('edit_customer/',edit_customer,name='edit_customer'),
    path('display_customer/',display_customer,name='display_customer'),
    path('display_customer/',display_customer,name='display_customer'),
    
    #products
    path('add_product/',add_product,name='add_product'),
     path('edit_product/',edit_product,name='edit_product'),
    path('display_product/',display_product,name='display_product'),
    
 
]

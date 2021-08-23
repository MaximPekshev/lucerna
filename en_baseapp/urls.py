from django.urls import path
from .views import en_show_index
from .views import en_show_products
from .views import en_show_about
from .views import en_show_contacts
from .views import en_show_production

urlpatterns = [    
    path('', en_show_index, name='en_show_index'),
    path('products/', en_show_products, name='en_show_products'),
    path('about/', en_show_about, name='en_show_about'),
    path('contacts/', en_show_contacts, name='en_show_contacts'),
    path('production/', en_show_production, name='en_show_production'),
    
]

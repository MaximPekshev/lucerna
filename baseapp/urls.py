from django.urls import path
from .views import show_index
from .views import show_products
from .views import show_about
from .views import show_contacts
from .views import show_production
from .views import send_contact_form

urlpatterns = [    
    path('', show_index, name='show_index'),
    path('products/', show_products, name='show_products'),
    path('about/', show_about, name='show_about'),
    path('contacts/', show_contacts, name='show_contacts'),
    path('production/', show_production, name='show_production'),
    path('send-contact-form/', send_contact_form, name='send_contact_form'),

]

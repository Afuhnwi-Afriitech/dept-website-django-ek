from django.urls import path

from main.views import *

urlpatterns = [
    path('', home_page, name='index'),
    path('features', features, name='features'),
    path('faq', faq, name='faq'),
    path('about-us', about_us, name='about-us'),
    path('contact-us', contact_us, name='contact-us'),
]
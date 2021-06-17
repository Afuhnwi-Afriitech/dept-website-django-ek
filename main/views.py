from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView


def home_page(request):
    return render(request, 'index.html')


def features(request):
    return render(request, 'features.html')


def faq(request):
    return render(request, 'faq.html')


def about_us(request):
    return render(request, 'about-us.html')


def contact_us(request):
    return render(request, 'contact-us.html')

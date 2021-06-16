

from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView


def home_page(request):
    return render(request, 'index.html')

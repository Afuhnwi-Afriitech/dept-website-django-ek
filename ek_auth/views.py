from django.contrib.auth.views import LoginView
from django.shortcuts import render
import sqlite3


# Create your views here.


def login_view(request):
    # logic of view will be implemented here

    return render(request, 'ek-login.html')


def register_view(request):
    user_info = request.POST
    for k in user_info.keys():
        print(user_info[k])
    return render(request, 'ek-register.html')

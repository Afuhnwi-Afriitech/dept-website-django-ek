from django.http import request
from django.urls import path

# importing views from views.p

from .views import login_view

urlpatterns = [
    path('login/', login_view, name='login')
]

from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView
from django.views.generic import ListView

from blog.models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'




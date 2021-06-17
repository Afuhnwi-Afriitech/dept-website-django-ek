from django.core.mail import send_mail
from django.http import BadHeaderError, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView


def home_page(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'profile.html')


def features(request):
    return render(request, 'features.html')


def courses(request):
    return render(request, 'courses.html')


def faq(request):
    return render(request, 'faq.html')


def gallery(request):
    return render(request, 'gallery.html')


def about_us(request):
    return render(request, 'about-us.html')


def contact_us(request):
    return render(request, 'contact-us.html')


def contact(request):
    if request.method == 'POST':
        form = request.POST
        #if form.is_valid():
        # subject = "Website Inquiry"
        subject = form['subject']
        body = {
            'name': form['name'],
            'email': form['email'],
            'message': form['message'],
        }
        message = "\n".join(body.values())

        try:
            send_mail(subject, message, 'elroykanye@gmail.com', ['elroykanye@gmail.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect("main:homepage")
    form = request.POST
    return render(request, "contact-us.html", {'form': form})

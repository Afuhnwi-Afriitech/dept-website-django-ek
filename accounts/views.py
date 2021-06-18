from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User


# Create your views here.

def signup(request):
    if request.method == "POST":
        try:
            User.objects.get(username=request.POST.get('username'))
            return render(request, 'registration.html', {
                'error': 'Username is already taken'
            })
        except User.DoesNotExist:
            user = User.objects.create_user(
                request.POST['username'],
                password=request.POST['password']
            )
            auth.login(request, user)
            return redirect('index')
    else:
        return render(request, 'registration.html')


'''
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if user is not None:
            auth.login(request, user)
            request.session['user_id'] = user
            return redirect('index')
        else:
            return render(request, 'login.html', {
                'error': 'Username or password is incorrect'
            })
    else:
        return render(request, 'login.html')
'''


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )

        if user is None:
            auth.login(request, user)
            request.session['user_id'] = user
            return redirect('index')
        else:
            return render(request, 'login.html', {
                'error': 'Username or password is incorrect'
            })
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':

        try:
            del request.session['user_id']
        except KeyError:
            pass
        auth.logout(request)
    print(request.session['user_id'])
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return redirect('index')

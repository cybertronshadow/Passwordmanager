import password
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from .filters import *


def loginpage(request):
    page = 'login'
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    context = {'page': page}

    return render(request, 'password/loginregister.html', context)


def logoutpage(request):
    logout(request)
    return redirect('login')


def registeruser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm()
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            user = authenticate(request, username=user.username,
                                password=request.POST['password'])

            if user is not None:
                login(request, user)
                return redirect('home')

    context = {'form': form, 'page': page}
    return render(request, 'password/loginregister.html', context)


@login_required(login_url='login')
def home(request):
    form = StoredPasswordForm()
    context = {'form': form}

    if request.method == 'POST':
        form = StoredPasswordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('storedpassword')
    return render(request, 'password/main.html', context)


@login_required(login_url='login')
def storedpassword(request):
    passwords = StoredPassword.objects.all()
    totalstoredpassword = passwords.count()
    myfilter = PasswordFilter(request.POST, queryset=passwords)
    passwords = myfilter.qs
    context = {'passwords': passwords,
               'totalstoredpassword': totalstoredpassword, 'myfilter': myfilter}
    return render(request, 'password/storedpassword.html', context)


@login_required(login_url='login')
def update(request, pk):
    password = StoredPassword.objects.get(id=pk)
    form = StoredPasswordForm(instance=password)
    if request.method == 'POST':
        form = StoredPasswordForm(request.POST, instance=password)
        if form.is_valid():
            form.save()
            return redirect('storedpassword')
    context = {'form': form}
    return render(request, 'password/update.html', context)


@login_required(login_url='login')
def delete(request, pk):
    password = StoredPassword.objects.get(id=pk)
    if request.method == 'POST':
        password.delete()
        return redirect('storedpassword')
    context = {'item': password}

    return render(request, 'password/delete.html', context)

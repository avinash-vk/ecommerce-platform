from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

from .forms import CreateUserForm

def landing_page(request):
    return render(request,'landingPage.htm')

def auth_type(request):
    return render(request,'auth.htm')

def seller_register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print("REGISTERED")
            user  = form.save()
            group = Group.objects.get(name = "seller")
            user.groups.add(group)
            return redirect('login')
    context = {'form' : form,}
    return render(request,'sellerRegister.htm',context)

def buyer_register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            print("REGISTERED")
            user  = form.save()
            group = Group.objects.get(name = "buyer")
            user.groups.add(group)
            return redirect('login')
    context = {
        'form' : form,
    }
    return render(request,'buyerRegister.htm',context)

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request,user)
            print("logged in")
            return redirect('landing-page')
        else:
            print("wrong password")
    return render(request,'signin.htm')

def logoutUser(request):
    logout(request)
    print("Logged out")
    return redirect('landing-page')

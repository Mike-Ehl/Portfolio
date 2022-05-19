from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm


#______________________________________________________
#HOME#
#------------------------------------------------------
def home(request):
    return render(request, 'basics/home.html', {})










#______________________________________________________
#LOGIN
#------------------------------------------------------
def user_login(request): 
    if request.method == "POST": 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect ('home')
        else:
            messages.success(request, "There was an error, try again")
            return redirect('user_login')
    return render (request, 'user_registration_app/user_login.html', {})









#______________________________________________________
#LOGOUT
#------------------------------------------------------
def user_logout(request):
    logout(request)
    messages.success(request, ("Logged Out"))
    return redirect('home')










#______________________________________________________
#REGISTER
#------------------------------------------------------



def user_register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate( username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successfull")
            return redirect('home')
    else:
        form = RegisterUserForm()

    return render (request, 'user_registration_app/user_register.html',{
    'form': form,
    })






#______________________________________________________
#LOGOUT
#------------------------------------------------------










def user_delete(request):
    return render(request, 'user_registration_app/user_delete.html', {})

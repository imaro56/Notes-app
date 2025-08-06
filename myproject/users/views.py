from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request,form.save())
            return redirect('notes:new')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html',{'form':form})

def signin_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('notes:list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/signin.html', {'form':form})

def signout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')

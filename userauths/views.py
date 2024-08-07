from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm



def home(request):
    return render(request, 'index.html')


#user Register
def register(request):
    form = UserCreationForm
    if request.method == 'POST':
        regform = UserCreationForm(request.POST)
        if regform.is_valid():
            regform.save()
            messages.success(request, 'Registration was successful!')
    return render(request, 'register.html', {"form": form})

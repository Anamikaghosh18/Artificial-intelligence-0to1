from django.shortcuts import render, redirect
from .forms import UserRegisterForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created! You can Login now!")
            return redirect('blog-home')

    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form' : form })



from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login ,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
# ... import other necessary functions for authentication, token generation, etc.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # ... handle password hashing, user creation, profile picture upload

            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            if(password1 != password2):
                messages.warning(request, "Password is not matched")
                return redirect('signup')
            
            
            user = form.save()
           
            login(request, user)
            return redirect('dashboard')  # Redirect to appropriate dashboard
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.user_type == 'Patient':
        return render(request, 'PatientDashboard.html', {'user': request.user})
    else:
        return render(request, 'DoctorDashboard.html', {'user': request.user})

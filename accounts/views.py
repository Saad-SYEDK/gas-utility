from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from requests.models import ServiceRequest
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt 

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/signup.html', {'form': form})

# User Dashboard (to view requests)
@login_required
def user_dashboard(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'accounts/dashboard.html', {'requests': requests})

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect("account")  # Redirect to account page
    else:
        form = RegisterForm()
    
    return render(request, "accounts/register.html", {"form": form})

@login_required
def account(request):
    return render(request, "accounts/account.html")

@csrf_exempt  # Disable CSRF for this view (optional, but prevents issues)
def custom_logout(request):
    """Logs out the user and redirects to login page."""
    if request.method in ['GET', 'POST']:  # Allow both GET and POST requests
        logout(request)
        return redirect('login')  # Redirect to login page after logout
    else:
        return redirect('account')  # If other methods are used, stay on account page
    
    
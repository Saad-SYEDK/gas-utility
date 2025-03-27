from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from requests.models import ServiceRequest
from django.contrib.auth.forms import UserCreationForm

# Signup View
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

# User Dashboard (to view requests)
@login_required
def user_dashboard(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'accounts/dashboard.html', {'requests': requests})

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after successful registration
            return redirect("account")  # Redirect to account page
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})

def account(request):
    return render(request, "accounts/account.html")


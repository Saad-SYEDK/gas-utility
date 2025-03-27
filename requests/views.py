from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm

# Create your views here.

@login_required
def service_request_list(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'requests/service_requests.html', {'request': requests})

def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'user': request.user})  # Pass user data
    return redirect("login")

@login_required
def submit_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.user = request.user  # Assign the logged-in user
            service_request.save()
            return redirect("track_requests")
    else:
        form = ServiceRequestForm()

    return render(request, "services/submit_request.html", {"form": form})



@login_required
def track_requests(request):
    user_requests = ServiceRequest.objects.filter(user=request.user)  # Filter by logged-in user
    return render(request, "services/track_requests.html", {"requests": user_requests})

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
    return render(request, 'home.html')

def submit_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")  # Redirect to home after submission
    else:
        form = ServiceRequestForm()
    return render(request, "submit_request.html", {"form": form})


def track_requests(request):
    requests = ServiceRequest.objects.all().order_by("-created_at")  # Show latest requests first
    return render(request, "track_requests.html", {"requests": requests})
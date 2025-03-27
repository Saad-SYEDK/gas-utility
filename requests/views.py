from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
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


# Check if user is staff
def is_staff(user):
    return user.is_staff

@login_required
@user_passes_test(is_staff)
def staff_dashboard(request):
    requests = ServiceRequest.objects.all()
    return render(request, "services/staff_dashboard.html", {"requests": requests})

@login_required
@user_passes_test(is_staff)
def update_request_status(request, request_id):
    request_obj = get_object_or_404(ServiceRequest, id=request_id)

    if request.method == "POST":
        new_status = request.POST.get("status")
        if new_status:
            request_obj.status = new_status
            request_obj.save()
            return redirect("staff_dashboard")

    return render(request, "services/update_request.html", {"request_obj": request_obj})
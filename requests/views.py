from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest

# Create your views here.

@login_required
def service_request_list(request):
    requests = ServiceRequest.objects.filter(user=request.user)
    return render(request, 'requests/service_requests.html', {'request': requests})


def home(request):
    return render(request, 'home.html')


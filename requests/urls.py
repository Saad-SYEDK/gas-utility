from django.urls import path
from .views import service_request_list

urlpatterns = [
    path('', service_request_list, name='service_requests'),
    
]

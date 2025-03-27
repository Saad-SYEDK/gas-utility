from django.urls import path
from .views import home, submit_request, track_requests, staff_dashboard, update_request_status

urlpatterns = [
    path('', home, name="home"),
    path("submit/", submit_request, name="submit_request"),
    path("track/", track_requests, name="track_requests"),
    path("staff-dashboard/", staff_dashboard, name="staff_dashboard"),
    path("update-request/<int:request_id>/", update_request_status, name="update_request_status"),

    
    
]

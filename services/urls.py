from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from requests import views  # Import your views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("submit/", views.submit_request, name="submit_request"),
    path("track/", views.track_requests, name="track_requests"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from requests import views  # Import your views

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Home Page
    path("", views.home, name="home"),

    # Service Request URLs
    path("submit/", views.submit_request, name="submit_request"),
    path("track/", views.track_requests, name="track_requests"),

    # Authentication URLs
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Include accounts URLs
    path("accounts/", include("accounts.urls")),
    
    path("requests/", include("requests.urls")),  # Include the `requests` app URL
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

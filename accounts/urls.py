from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, account, custom_logout
from django.contrib.auth.views import LogoutView, LoginView

urlpatterns = [
    path("register/", register, name="register"),
    path("account/", account, name="account"),
    path("login/", LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]

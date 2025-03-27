from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register, account

urlpatterns = [
    path("register/", register, name="register"),
    path("account/", account, name="account"),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]

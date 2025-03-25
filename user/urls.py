from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(
        template_name="auth/login.html",
        next_page=reverse_lazy("course_list")
    ), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    
    # Password reset URLs
    path("password_reset/", auth_views.PasswordResetView.as_view(
        template_name="auth/password_reset.html"
    ), name="password_reset"),
    path("password_reset/done/", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    
    # Password change URLs
    path("password_change/", auth_views.PasswordChangeView.as_view(
        success_url=reverse_lazy("password_change_done")
    ), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(), name="password_change_done"),
]

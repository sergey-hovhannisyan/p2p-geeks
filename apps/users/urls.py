from django.urls import path
from . import views as user_views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView

urlpatterns = [
    path("register/", user_views.register, name="register"),
    path("profile/", user_views.profile, name="profile"),
    path("connect/", user_views.connect, name="connect"),
    path("review/", user_views.review, name="review"),
    path("interviews/", user_views.interviews, name="interviews"),
    path("schedule/", user_views.schedule, name="schedule"),
    path("login/", user_views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="index.html"), name="logout"), 
    path("base/", TemplateView.as_view(template_name="users_base.html"), name="base"),
]
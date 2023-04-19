"""
p2p-geeks URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from apps.users import views as user_views
from apps.posts import urls as post_urls


urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", user_views.register, name="register"),
    path("profile/", user_views.profile, name="profile"),
    path("connect/", user_views.connect, name="connect"),
    path("login/", user_views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="index.html"), name="logout"),
    path("signedin/", cache_page(60 * 15)(TemplateView.as_view(template_name="signed_in_home.html")), name="signed_in_home"),
    path("", cache_page(60 * 15)(TemplateView.as_view(template_name="index.html")), name="index")
] + post_urls.urlpatterns


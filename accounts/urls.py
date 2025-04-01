from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from accounts import views

# dev_9
app_name = "accounts"

urlpatterns = [
    path("login/", views.login_user, name="login_user"),
]

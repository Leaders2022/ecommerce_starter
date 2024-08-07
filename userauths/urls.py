from django.urls import path, include
from django.conf import settings
from userauths import views
from django.conf.urls.static import static

app_name = 'userauths'
urlpatterns = [
    path("register/", views.register, name="register"),
]

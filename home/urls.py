from django.urls import path
from . import views


app_name = "home"

urlpatterns = [
    path("", views.home, name="home"),
    path("works/", views.works, name="works"),
    path("works/<slug:slug>/", views.work_detail, name="work_detail"),
    path("approach/", views.approach, name="approach"),
    path("services/", views.services, name="services"),
    path("contact/", views.contact, name="contact"),
]

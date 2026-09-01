from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("services/<int:pk>/", views.service_detail, name="service_detail"),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path("equipment/", views.equipment, name="equipment"),
    path("certificates/", views.certificates, name="certificates"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
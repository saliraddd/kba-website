from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path("", views.home, name="home"),
    path("services/", views.services, name="services"),
    path("services/ndt/", views.ndt_service, name="ndt_service"),
    path("services/ndt-level-3/", views.ndt_level3, name="ndt_level3"),
    path("services/welding-engineering/", views.welding_engineering, name="welding_engineering"),
    path("services/technical-inspection/", views.technical_inspection, name="technical_inspection"),
    path("services/welding-inspection/", views.welding_inspection, name="welding_inspection"),
    path("services/<int:pk>/", views.service_detail, name="service_detail"),
    path("projects/", views.projects, name="projects"),
    path("projects/<int:pk>/", views.project_detail, name="project_detail"),
    path("equipment/", views.equipment, name="equipment"),
    path("certificates/", views.certificates, name="certificates"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
]
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import (
    Certificate,
    Equipment,
    Project,
    Service,
)


def home(request):
    context = {
        "services": Service.objects.filter(is_featured=True)[:6],
        "projects": Project.objects.filter(is_featured=True)[:6],
        "equipment": Equipment.objects.all()[:6],
        "certificates": Certificate.objects.all()[:6],
    }

    return render(request, "website/home.html", context)


def services(request):
    context = {
        "services": Service.objects.all(),
    }

    return render(request, "website/services.html", context)


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)

    related_projects = service.projects.all()[:6]

    context = {
        "service": service,
        "related_projects": related_projects,
    }

    return render(
        request,
        "website/service_detail.html",
        context,
    )


def projects(request):
    context = {
        "projects": Project.objects.prefetch_related("services"),
    }

    return render(request, "website/projects.html", context)


def project_detail(request, pk):
    project = get_object_or_404(
        Project.objects.prefetch_related("services"),
        pk=pk,
    )

    context = {
        "project": project,
    }

    return render(
        request,
        "website/project_detail.html",
        context,
    )


def equipment(request):
    context = {
        "equipment": Equipment.objects.all(),
    }

    return render(request, "website/equipment.html", context)


def certificates(request):
    context = {
        "certificates": Certificate.objects.all(),
    }

    return render(request, "website/certificates.html", context)


def about(request):
    return render(request, "website/about.html")


def contact(request):

    if request.method == "POST":

        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "پیام شما با موفقیت ثبت شد. کارشناسان ما با شما تماس خواهند گرفت.",
            )

            return redirect("website:contact")

    else:
        form = ContactForm()

    return render(
        request,
        "website/contact.html",
        {"form": form},
    )
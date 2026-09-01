from django.contrib import admin

from .models import (
    Service,
    Project,
    Equipment,
    Certificate,
    ContactMessage,
)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "short_name",
        "category",
        "is_featured",
        "order",
    )

    list_filter = (
        "category",
        "is_featured",
    )

    search_fields = (
        "title",
        "short_name",
    )

    list_editable = (
        "is_featured",
        "order",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "client",
        "location",
        "project_date",
        "is_featured",
    )

    list_filter = (
        "is_featured",
        "project_date",
    )

    search_fields = (
        "title",
        "client",
        "location",
    )

    filter_horizontal = (
        "services",
    )


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "model",
        "manufacturer",
        "order",
    )

    search_fields = (
        "name",
        "model",
        "manufacturer",
    )

    list_editable = (
        "order",
    )


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "issuer",
        "issue_date",
        "order",
    )

    search_fields = (
        "title",
        "issuer",
    )

    list_editable = (
        "order",
    )
    
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "company",
        "phone",
        "subject",
        "created_at",
        "is_read",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    search_fields = (
        "name",
        "company",
        "phone",
        "email",
        "message",
    )

    list_editable = (
        "is_read",
    )

    readonly_fields = (
        "created_at",
    )
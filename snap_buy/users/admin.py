from django.contrib import admin

from .models import Address
from .models import User


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "private_metadata",
        "metadata",
        "first_name",
        "last_name",
        "company_name",
        "street_address_1",
        "street_address_2",
        "city",
        "city_area",
        "postal_code",
        "country",
        "country_area",
        "phone",
        "validation_skipped",
    )
    list_filter = ("validation_skipped",)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "last_login",
        "is_superuser",
        "is_staff",
        "is_active",
        "name",
        "email",
        "is_confirmed",
        "last_confirm_email_request",
        "note",
        "date_joined",
        "updated_at",
        "last_password_reset_request",
        "avatar",
        "jwt_token_key",
        "language_code",
        "search_document",
        "uuid",
        "default_shipping_address",
        "default_billing_address",
    )
    list_filter = (
        "last_login",
        "is_superuser",
        "is_staff",
        "is_active",
        "is_confirmed",
        "last_confirm_email_request",
        "date_joined",
        "updated_at",
        "last_password_reset_request",
        "default_shipping_address",
        "default_billing_address",
    )
    raw_id_fields = ("groups", "user_permissions", "addresses")
    search_fields = ("name",)
    date_hierarchy = "updated_at"

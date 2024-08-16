from rest_framework import serializers

from snap_buy.users.models import Address
from snap_buy.users.models import User


class AddressSerializer(serializers.HyperlinkedModelSerializer[Address]):
    class Meta:
        model = Address
        fields = [
            "url",
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
        ]
        extra_kwargs = {
            "url": {"view_name": "api:address-detail", "lookup_field": "pk"},
        }


class UserSerializer(serializers.HyperlinkedModelSerializer[User]):
    addresses = AddressSerializer(many=True)

    class Meta:
        model = User
        exclude = [
            "jwt_token_key",
        ]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "pk"},
            "addresses": {"view_name": "api:address-detail", "lookup_field": "pk"},
        }

from rest_framework import serializers

from snap_buy.channel.models import Channel


class ChannelSerializer(serializers.HyperlinkedModelSerializer[Channel]):
    class Meta:
        model = Channel
        fields = [
            "name",
            "is_active",
            "slug",
            "currency_code",
            "default_country",
            "allocation_strategy",
            "order_mark_as_paid_strategy",
            "default_transaction_flow_strategy",
            "automatically_confirm_all_new_orders",
            "allow_unpaid_orders",
            "automatically_fulfill_non_shippable_gift_card",
            "expire_orders_after",
            "delete_expired_orders_after",
            "include_draft_order_in_voucher_usage",
            "use_legacy_error_flow_for_checkout",
        ]
        extra_kwargs = {
            "url": {"view_name": "api:channel-detail", "lookup_field": "pk"},
        }

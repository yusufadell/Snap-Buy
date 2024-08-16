from rest_framework.mixins import ListModelMixin
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import GenericViewSet

from snap_buy.channel.api.serializers import ChannelSerializer
from snap_buy.channel.models import Channel


class ChannelViewSet(
    RetrieveModelMixin,
    ListModelMixin,
    UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = ChannelSerializer
    queryset = Channel.objects.all()

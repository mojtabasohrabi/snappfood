from rest_framework.request import Request
from .models import Order
from .serializers import OrderSerializer
from rest_framework import generics, mixins


class OrdersCreateMixinApiView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request: Request):
        return self.create(request)


class OrdersListMixinApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request: Request):
        return self.list(request)

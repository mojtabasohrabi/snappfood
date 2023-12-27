from rest_framework.request import Request
from .models import Vendor
from .serializers import VendorSerializer
from rest_framework import generics, mixins


class VendorsCreateMixinApiView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def post(self, request: Request):
        return self.create(request)


class VendorsListMixinApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

    def get(self, request: Request):
        return self.list(request)

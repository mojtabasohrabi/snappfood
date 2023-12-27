from rest_framework.request import Request
from .models import Vendor
from .serializers import VendorSerializer
from rest_framework import generics, mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date, datetime, timedelta
from orders.models import Order
from django.db.models import Sum



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


class VendorsSumWeekliDelayApiView(APIView):

    @staticmethod
    def calculate_week():
        today = date.today()
        seven_day_before = today - timedelta(days=7)
        return seven_day_before

    def get(self, request: Request):
        seven_day_before = self.calculate_week()
        sum_delay_for_each_vendor = (Order.objects.filter(created__gte=seven_day_before)
                                 .values('vendor').distinct()
                                 .annotate(sum_delays_in_this_week_by_minutus=Sum('delay')))

        return Response({'data': sum_delay_for_each_vendor}, status.HTTP_200_OK)

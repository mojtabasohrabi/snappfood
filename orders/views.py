import random

from .models import Order, Trip, DelayReport
from .serializers import OrderSerializer, TripSerializer, DelayReportSerializer
from rest_framework import viewsets, generics
from rest_framework.exceptions import ValidationError
import datetime
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class TripsCreateGenericApiView(generics.CreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class OrdersViewSetApiView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # pagination_class = LimitOffsetPagination


class TripsViewSetApiView(viewsets.ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer


class DelayReportViewSetApiView(viewsets.ModelViewSet):
    queryset = DelayReport.objects.all()
    serializer_class = DelayReportSerializer


class OrderDelayReportApiView(APIView):

    @staticmethod
    def get_order(order_id):
        return Order.objects.filter(id=order_id).values('delivery_time', 'updated', 'delay').first()

    @staticmethod
    def update_order_delivery_time(order_id, new_delay_time):
        order = Order.objects.get(pk=order_id)
        order.delay = new_delay_time
        order.updated = timezone.now()
        order.save()

    @staticmethod
    def existence_open_delay_report(order_id):
        delay_report = DelayReport.objects.filter(order__id=order_id, status__in=['WAIT_FOR_AGENT', 'IN_PROGRESS'])
        if delay_report:
            return True
        return False

    @staticmethod
    def create_delay_report(order_id):
        order = Order.objects.get(pk=order_id)
        query = DelayReport(order=order)
        query.save()

    def post(self, request, *args, **kwargs):
        order_id = request.data.get('order', 0)
        if order_id:
            order = self.get_order(order_id)
        else:
            raise ValidationError("There was a problem!")

        if order:

            delivery_time_by_delay = order.get('delivery_time') + order.get('delay')
            updated = order.get('updated')

            if datetime.timedelta(minutes=delivery_time_by_delay) + updated < timezone.now():
                order_trip = Trip.objects.filter(order__id=order_id).values('status').first()

                if order_trip and order_trip.get('status') in ['ASSIGNED', 'AT_VENDOR', 'PICKED']:
                    new_delay_time = order.get('delay') + random.randint(10, 30)
                    self.update_order_delivery_time(order_id, new_delay_time)
                    return Response({'new_delivery_time': new_delay_time}, status.HTTP_200_OK)

                elif not order_trip or order_trip.get('status') == 'DELIVERED':
                    if not self.existence_open_delay_report(order_id):
                        self.create_delay_report(order_id)
                    return Response({'message': 'your report is in progress'}, status.HTTP_200_OK)
                else:
                    return Response({'error': 'There was a problem!'}, status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'order in progress!'}, status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'order not found!'}, status.HTTP_404_NOT_FOUND)

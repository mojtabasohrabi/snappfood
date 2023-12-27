from rest_framework import serializers
from .models import Order, Trip, DelayReport


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'


class DelayReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DelayReport
        fields = '__all__'

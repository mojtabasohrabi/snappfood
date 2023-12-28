from rest_framework import serializers
from .models import Agent
from orders.models import DelayReport


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = '__all__'


class DelayReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DelayReport
        fields = '__all__'

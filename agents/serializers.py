from rest_framework import serializers
from .models import Agent


class AgentSerializer(serializers.ModelSerializer):

    # def validate_priority(self, priority):
    #     if priority < 10 or priority > 20:
    #         raise serializers.ValidationError('priority is not ok')
    #     return priority

    class Meta:
        model = Agent
        fields = '__all__'

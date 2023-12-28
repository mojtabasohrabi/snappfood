from rest_framework.request import Request
from .models import Agent
from orders.models import DelayReport
from .serializers import AgentSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class AgentsCreateMixinApiView(generics.CreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class AgentsListMixinApiView(generics.ListAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer


class CheckDelayReportApiView(APIView):
    @staticmethod
    def has_open_delay_report(agent_id):
        delay_report_by_this_agent = DelayReport.objects.filter(agent_id=agent_id, status='IN_PROGRESS')
        if delay_report_by_this_agent:
            return True
        return False

    @staticmethod
    def get_agent(agent_id):
        return Agent.objects.filter(id=agent_id).first()

    def assign_first_open_delay_report(self, agent_id):
        agent = self.get_agent(agent_id)
        delay_report = DelayReport.objects.filter(status='WAIT_FOR_AGENT').first()
        if delay_report:
            delay_report.agent = agent
            delay_report.status = 'IN_PROGRESS'
            delay_report.save()
            return delay_report.id
        return False

    def post(self, request: Request):
        agent_id = request.data.get('agent', 0)
        if agent_id:
            agent = self.get_agent(agent_id)
        else:
            return Response({'error': 'there is a problem!'}, status.HTTP_400_BAD_REQUEST)

        if agent:
            if self.has_open_delay_report(agent_id):
                return Response({'error': 'There is a open delay report for you! first finish it'}, status.HTTP_200_OK)

            delay_report_assigned = self.assign_first_open_delay_report(agent_id)
            if delay_report_assigned:
                return Response({'delay_report_assigned': delay_report_assigned}, status.HTTP_200_OK)
            else:
                return Response({'error': 'there isn`t open delay report'}, status.HTTP_200_OK)
        else:
            return Response({'error': 'agent not found!'}, status.HTTP_404_NOT_FOUND)

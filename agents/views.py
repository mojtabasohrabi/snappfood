from rest_framework.request import Request
from .models import Agent
from .serializers import AgentSerializer
from rest_framework import generics, mixins


class AgentsCreateMixinApiView(mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    def post(self, request: Request):
        return self.create(request)


class AgentsListMixinApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    def get(self, request: Request):
        return self.list(request)

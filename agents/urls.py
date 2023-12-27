from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('create/', views.AgentsCreateMixinApiView.as_view()),
    path('list/', views.AgentsListMixinApiView.as_view())
]
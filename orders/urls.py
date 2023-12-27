from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('create/', views.OrdersCreateMixinApiView.as_view()),
    path('list/', views.OrdersListMixinApiView.as_view()),
]
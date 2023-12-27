from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('order', views.OrdersViewSetApiView)
router.register('trip', views.TripsViewSetApiView)
router.register('delay-report-list', views.DelayReportViewSetApiView)

urlpatterns = [
    path('ready/', views.TripsCreateGenericApiView.as_view()),
    path('delay-report/', views.OrderDelayRreportApiView.as_view()),
]

urlpatterns += router.urls
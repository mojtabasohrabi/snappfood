from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

urlpatterns = [
    path('create/', views.VendorsCreateMixinApiView.as_view()),
    path('list/', views.VendorsListMixinApiView.as_view()),
    path('sum-weekli-delay/', views.VendorsSumWeekliDelayApiView.as_view())
]
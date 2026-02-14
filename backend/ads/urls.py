from django.contrib import admin
from django.urls import path, include
from .views import dashboard_page, ads_dashboard, facebook_live_ads

urlpatterns = [
    path('', dashboard_page),
    path('dashboard/', ads_dashboard),
    path('facebook-live/', facebook_live_ads),
]
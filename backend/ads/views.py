from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from django.http import JsonResponse
import requests

from .models import FacebookAdStat, WhatsAppLead

@api_view(['GET'])
def ads_dashboard(request):

    fb_stats = FacebookAdStat.objects.all().order_by('-date')[:7]
    wa_leads = WhatsAppLead.objects.all().order_by('-created_at')[:10]

    fb_data = []
    for f in fb_stats:
        fb_data.append({
            "date": f.date,
            "impressions": f.impressions,
            "clicks": f.clicks,
            "spend": f.spend
        })

    wa_data = []
    for w in wa_leads:
        wa_data.append({
            "phone": w.phone,
            "message": w.message,
            "time": w.created_at
        })

    return Response({
        "facebook": fb_data,
        "whatsapp": wa_data
    })


@api_view(['GET'])
def facebook_live_ads(request):

    url = f"https://graph.facebook.com/v19.0/{settings.FB_AD_ACCOUNT_ID}/insights"

    params = {
        "fields": "campaign_name,impressions,clicks,spend",
        "date_preset": "maximum",
        "access_token": settings.FB_ACCESS_TOKEN
    }

    response = requests.get(url, params=params)
    return Response(response.json())




def dashboard_page(request):
    return render(request, 'dashboard.html')
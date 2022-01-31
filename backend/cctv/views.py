from django.shortcuts import render

# Create your views here.
from regi.fcm_notification import send_to_firebase_cloud_messaging


def cctv(request):
    return render(request, 'cctv/mqtt.html')


def modelresult(request):
    send_to_firebase_cloud_messaging()
    return render(request, 'cctv/modelresult.html')

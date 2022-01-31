from django.conf.urls.static import static
from django.urls import path

from backend import settings
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('postcreate', views.postcreate, name='picsave'),
    path('getgraph1/', views.getgraph1, name='getgraph1'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

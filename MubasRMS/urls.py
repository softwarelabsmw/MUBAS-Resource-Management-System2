"""MubasRMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Import configuration settings for MEDIA_URL & STATIC_URL
from django.conf import settings
from django.conf.urls.static import static

from django.views.generic.base import TemplateView

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path('users/', include('django.contrib.auth.urls')),  # URLs  to ALL_AUTH APP
    path('users/', include('usersapp.urls')),  # ULRs to the USERSAPP
    path('', include('reservationapp.urls')),  # ULRs to the reservation App
    path('', TemplateView.as_view(template_name='home.html'), name='home'),  # HomePage Url
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),  # HomePage Url
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Media_url configuration

admin.site.site_header = "MUBAS Resource Reservation Admin"
admin.site.site_title = "MUBAS Resource Reservation Admin"
admin.site.index_title = "MUBAS Resource Reservation System"
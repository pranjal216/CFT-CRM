from django.contrib import admin
from django.urls import path, include
from apps.client import views
from ..meeting.views import L_Meeting

app_name = 'client'
urlpatterns = [
    path('', views.AddClientView.as_view(), name='add_client_form'),
]
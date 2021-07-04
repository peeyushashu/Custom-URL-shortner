from django.contrib import admin
from django.urls import path, include
from .views import AddURL, Redirector

app_name = 'CustomURLCreator'

urlpatterns = [
    path('add-url/', AddURL.as_view(), name='add-url'),
    path('1/<slug>/', Redirector.as_view(), name='Redirect'),
]

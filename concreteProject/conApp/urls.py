from django.conf.urls import url
from conApp import views
from django.urls import path

app_name = 'conApp'

urlpatterns = [
    path('', views.dataUploadView.as_view(), name = 'con'),
    
]

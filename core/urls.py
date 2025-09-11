from django.urls import path
from django.contrib.auth import views

from .views import  IndexView

app_name = 'core'

urlpatterns = [
    
    path('', IndexView.as_view(), name='index'),
    
    
]

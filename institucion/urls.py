
from django.urls import path
from django.contrib.auth import views

from .views import InstitucionCreateView

app_name = 'institucion'

urlpatterns = [
    path('institucion/nueva/', InstitucionCreateView.as_view(), name='institucion_create'),
    
]

from django.urls import path
from django.contrib.auth import views

from .views import PersonaCreateView

app_name = 'persona'

urlpatterns = [

    path('persona/nueva/', PersonaCreateView.as_view(), name='persona_create'),
    
]

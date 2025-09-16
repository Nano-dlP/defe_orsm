from django.urls import path
from django.contrib.auth import views
from .views import ExpedientePresencialCreateView, ExpedienteJudicialCreateView, MedioIngresoSelectView, ExpedienteOficioCreateView


app_name = 'expediente'





urlpatterns = [
    path('expediente-presencial/nuevo/', ExpedientePresencialCreateView.as_view(), name='expediente_presencial_create'),
    path('expediente-judicial/nuevo/', ExpedienteJudicialCreateView.as_view(), name='expediente_judicial_create'),
    path('medio-ingreso/', MedioIngresoSelectView.as_view(), name='medio_ingreso_select'),
    path('expediente-oficio/nuevo/', ExpedienteOficioCreateView.as_view(), name='expediente_oficio_create'),
    #path('expediente-presencial/<int:pk>/', ExpedientePresencialDetailView.as_view(), name='expediente_presencial_detail'),
]
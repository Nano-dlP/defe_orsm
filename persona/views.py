from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import CreateView
from .models import Persona
from .forms import PersonaForm
from django.urls import reverse_lazy




class PersonaCreateView(LoginRequiredMixin, CreateView):
    model = Persona
    template_name = "persona/persona_crear.html"
    form_class = PersonaForm
    success_url = reverse_lazy('core:index')
    context_object_name = 'personas'
    login_url = 'core:login'
    
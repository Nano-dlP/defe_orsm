

from django.views.generic import CreateView
from .models import Persona
from .forms import PersonaForm
from django.urls import reverse_lazy




class PersonaCreateView(CreateView):
    model = Persona
    template_name = "persona/persona_crear.html"
    form_class = PersonaForm
    success_url = reverse_lazy('core:index')
    context_object_name = 'personas'
    
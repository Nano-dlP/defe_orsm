
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import ExpedienteForm, ExpedienteDocumentoFormSet
from .models import Expediente, ExpedientePersona, Persona, Rol, ExpedienteDocumento

class ExpedienteCreateView(CreateView):
    model = Expediente
    form_class = ExpedienteForm
    template_name = 'expediente/expediente_crear.html'
    success_url = reverse_lazy('core:index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['personas'] = Persona.objects.all()
        context['roles'] = Rol.objects.all()
        if self.request.method == 'POST':
            context['documento_formset'] = ExpedienteDocumentoFormSet(self.request.POST, self.request.FILES, queryset=ExpedienteDocumento.objects.none())
        else:
            context['documento_formset'] = ExpedienteDocumentoFormSet(queryset=ExpedienteDocumento.objects.none())
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        documento_formset = context['documento_formset']
        response = super().form_valid(form)
        persona_id = self.request.POST.get('persona')
        rol_id = self.request.POST.get('rol')
        if persona_id and rol_id:
            ExpedientePersona.objects.create(
                expediente=self.object,
                persona_id=persona_id,
                rol_id=rol_id
            )
        if documento_formset.is_valid():
            for doc_form in documento_formset:
                if doc_form.cleaned_data.get('archivo'):
                    doc = doc_form.save(commit=False)
                    doc.expediente = self.object
                    doc.save()
        return response

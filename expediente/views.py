from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, FormView
from django.forms import modelformset_factory
from .models import (ExpedienteJudicialDocumento, 
                    ExpedientePresencialDocumento,
                    ExpedienteOficioDocumento, 
                    ExpedientePersona, 
                    Rol, 
                    ExpedienteInstitucion,
                    ExpedienteOficioso
)

from .forms import (MedioIngresoForm,   
                    
                    ExpedientePresencialForm, 
                    ExpedientePresencialDocumentoFormSet, 
                    ExpedientePresencialDocumentoForm, 
                    
                    ExpedienteJudicialForm, 
                    ExpedienteJudicialDocumentoFormSet, 
                    ExpedienteJudicialDocumentoForm,
                    
                    ExpedienteOficioForm,
                    ExpedienteOficioDocumentoFormSet,
                    ExpedienteOficioDocumentoForm
                    
                    )

# Paso 1: Selección del Medio de Ingreso
class MedioIngresoSelectView(LoginRequiredMixin, FormView):
    template_name = 'expediente/medio_ingreso.html'
    form_class = MedioIngresoForm
    login_url = 'core:login'

    def get_initial(self):
        initial = super().get_initial()
        initial['medio_ingreso'] = 1  # ID por defecto
        return initial
    
    
    def form_valid(self, form):
        medio_ingreso_id = form.cleaned_data['medio_ingreso'].id

        if medio_ingreso_id in [1,] :
            return redirect('expediente:expediente_presencial_create', medio_id=medio_ingreso_id)
        elif  medio_ingreso_id in [2, 3, 4, 5, 6] :
            return redirect('expediente:expediente_create_oficio', medio_id=medio_ingreso_id)
        elif  medio_ingreso_id in [7,] :
            return redirect('expediente:expediente_create', medio_id=medio_ingreso_id)
        else:
            return redirect('expediente:medio_ingreso_select')



    login_url = 'core:login'

    def get(self, request, pk):
        expediente = get_object_or_404(Expediente, pk=pk)
        medio = expediente.medio_ingreso.medio_ingreso if expediente.medio_ingreso else ""

        # Redirigir a la vista correspondiente según medio de ingreso
        if medio == "DEMANDA ESPONTANEA":
            return redirect('expediente:demanda_espontanea_update', pk=pk)
        elif medio == "OFICIO POR MAIL":
            return redirect('expediente:oficio_update', pk=pk)
        elif medio == "Secretaria":
            return redirect('expediente:secretaria_update', pk=pk)
        else:
            messages.error(request, "No se pudo determinar el tipo de expediente.")
            return redirect('expediente:expediente_list')


class ExpedientePresencialCreateView(LoginRequiredMixin, View):
    template_name = 'expediente/expediente_presencial_form.html'

    def get(self, request):
        expediente_form = ExpedientePresencialForm()
        documento_formset = ExpedientePresencialDocumentoFormSet(queryset=ExpedientePresencialDocumento.objects.none())
        return render(request, self.template_name, {
            'form': expediente_form,
            'documento_formset': documento_formset
        })

    def post(self, request):
        expediente_form = ExpedientePresencialForm(request.POST)
        documento_formset = ExpedientePresencialDocumentoFormSet(
            request.POST, request.FILES,
            queryset=ExpedientePresencialDocumento.objects.none()
        )

        if expediente_form.is_valid() and documento_formset.is_valid():
            expediente = expediente_form.save()

            # Crear ExpedientePersona con rol id=1
            persona = expediente_form.cleaned_data['persona']
            rol = Rol.objects.get(pk=1)
            ExpedientePersona.objects.create(
                expediente=expediente,
                persona=persona,
                rol=rol
            )

            # Guardar documentos del formset
            for doc_form in documento_formset:
                if doc_form.cleaned_data and not doc_form.cleaned_data.get('DELETE', False):
                    documento = doc_form.save(commit=False)
                    documento.expediente = expediente
                    documento.save()

            return redirect('core:index')
        else:
            return render(request, self.template_name, {
                'form': expediente_form,
                'documento_formset': documento_formset
            })


class ExpedienteJudicialCreateView(LoginRequiredMixin, View):
    template_name = 'expediente/expediente_judicial_form.html'

    def get(self, request):
        expediente_form = ExpedienteJudicialForm()
        documento_formset = ExpedienteJudicialDocumentoFormSet(queryset=ExpedienteJudicialDocumento.objects.none())
        return render(request, self.template_name, {
            'form': expediente_form,
            'documento_formset': documento_formset
        })

    def post(self, request):
        expediente_form = ExpedienteJudicialForm(request.POST)
        documento_formset = ExpedienteJudicialDocumentoFormSet(
            request.POST, request.FILES,
            queryset=ExpedienteJudicialDocumento.objects.none()
        )

        if expediente_form.is_valid() and documento_formset.is_valid():
            expediente = expediente_form.save()

            # Crear ExpedienteInstitucion con rol id=2
            institucion = expediente_form.cleaned_data['institucion']
            rol = Rol.objects.get(pk=2)
            ExpedienteInstitucion.objects.create(
                expediente=expediente,
                institucion=institucion,
                rol=rol
            )

            # Guardar documentos del formset
            for doc_form in documento_formset:
                if doc_form.cleaned_data and not doc_form.cleaned_data.get('DELETE', False):
                    documento = doc_form.save(commit=False)
                    documento.expediente = expediente
                    documento.save()

            return redirect('core:index')
        else:
            return render(request, self.template_name, {
                'form': expediente_form,
                'documento_formset': documento_formset
            })



class ExpedienteOficioCreateView(LoginRequiredMixin, View):
    template_name = 'expediente/expediente_oficio_form.html'

    def get(self, request):
        expediente_form = ExpedienteOficioForm()
        documento_formset = ExpedienteOficioDocumentoFormSet(queryset=ExpedienteOficioDocumento.objects.none())
        return render(request, self.template_name, {
            'form': expediente_form,
            'documento_formset': documento_formset
        })

    def post(self, request):
        expediente_form = ExpedienteOficioForm(request.POST)
        documento_formset = ExpedienteOficioDocumentoFormSet(
            request.POST, request.FILES,
            queryset=ExpedienteOficioDocumento.objects.none()
        )

        if expediente_form.is_valid() and documento_formset.is_valid():
            expediente = expediente_form.save()

            # Crear ExpedienteOficio con rol id=3
            usuario_solicitante = expediente_form.cleaned_data['usuario_solicitante']
            rol = Rol.objects.get(pk=3)
            ExpedienteOficioso.objects.create(
                expediente=expediente,
                usuario_solicitante=usuario_solicitante,
                rol=rol
            )

            # Guardar documentos del formset
            for doc_form in documento_formset:
                if doc_form.cleaned_data and not doc_form.cleaned_data.get('DELETE', False):
                    documento = doc_form.save(commit=False)
                    documento.expediente = expediente
                    documento.save()

            return redirect('core:index')
        else:
            return render(request, self.template_name, {
                'form': expediente_form,
                'documento_formset': documento_formset
            })
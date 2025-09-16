from django import forms

from .models import(MedioIngreso, 
                    ExpedienteJudicial, 
                    ExpedientePresencial, 
                    ExpedienteOficio,
                    
                    ExpedientePresencialDocumento, 
                    ExpedienteJudicialDocumento, 
                    ExpedienteOficioDocumento
                    )

from django.forms import modelformset_factory


class MedioIngresoForm(forms.Form):
    medio_ingreso = forms.ModelChoiceField(
        queryset=MedioIngreso.objects.all(),
        label="Medio de Ingreso",
        widget=forms.Select(attrs={'class': 'form-control'})
    )



class ExpedientePresencialDocumentoForm(forms.ModelForm):
    class Meta:
        model = ExpedientePresencialDocumento
        fields = ['nombre', 'archivo']
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre del documento'}
            ),
            'archivo': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
        }

# Formset para múltiples documentos
ExpedientePresencialDocumentoFormSet = modelformset_factory(
    ExpedientePresencialDocumento,
    form=ExpedientePresencialDocumentoForm,
    extra=2,         # cantidad de formularios vacíos a mostrar
    can_delete=True   # permite borrar documentos existentes
)


class ExpedienteJudicialDocumentoForm(forms.ModelForm):
    class Meta:
        model = ExpedienteJudicialDocumento
        fields = ['nombre', 'archivo']
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre del documento'}
            ),
            'archivo': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
        }


# Formset para múltiples documentos
ExpedienteJudicialDocumentoFormSet = modelformset_factory(
    ExpedienteJudicialDocumento,
    form=ExpedienteJudicialDocumentoForm,
    extra=2,         # cantidad de formularios vacíos a mostrar
    can_delete=True   # permite borrar documentos existentes
)


class ExpedienteOficioDocumentoForm(forms.ModelForm):
    class Meta:
        model = ExpedienteOficioDocumento
        fields = ['nombre', 'archivo']
        widgets = {
            'nombre': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Ingrese nombre del documento'}
            ),
            'archivo': forms.ClearableFileInput(
                attrs={'class': 'form-control'}
            ),
        }

# Formset para múltiples documentos
ExpedienteOficioDocumentoFormSet = modelformset_factory(
    ExpedienteOficioDocumento,
    form=ExpedienteOficioDocumentoForm,
    extra=2,         # cantidad de formularios vacíos a mostrar
    can_delete=True   # permite borrar documentos existentes
)


class ExpedientePresencialForm(forms.ModelForm):
    class Meta:
        model = ExpedientePresencial
        fields = [
            'fecha_creacion',
            'sede',
            'medio_ingreso',
            'tipo_solicitud',
            'estado_expediente',
            'grupo_etario',
            'edad_persona',
            'situacion_habitacional_hist',
            'resumen_intervencion',
            'observaciones',
            'persona',
        ]
        labels = {
            'fecha_creacion': 'Fecha de creación',
            'sede': 'Sede',
            'medio_ingreso': 'Medio de ingreso',
            'tipo_solicitud': 'Tipo de solicitud',
            'estado_expediente': 'Estado del expediente',
            'grupo_etario': 'Grupo etario',
            'edad_persona': 'Edad de la persona',
            'situacion_habitacional_hist': 'Situación Habitacional Histórica',
            'resumen_intervencion': 'Resumen de intervención',
            'observaciones': 'Observaciones',
            'persona': 'Persona',
            
        }
        widgets = {
            'fecha_creacion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'observaciones': forms.Textarea(attrs={'class': 'form-control custom-textarea', 'rows': 3}),
            # Puedes agregar widgets personalizados para otros campos aquí si lo necesitas
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'observaciones':
                continue  # Ya está personalizado en widgets
            elif name == 'fecha_creacion':
                continue  # Ya está personalizado en widgets
            else:
                field.widget.attrs.update({
                    'class': 'form-control',
                    'style': 'text-transform: uppercase;',
                })



class ExpedienteJudicialForm(forms.ModelForm):
    class Meta:
        model = ExpedienteJudicial
        fields = [
            'fecha_creacion',
            'sede',
            'institucion',
            'medio_ingreso',
            'tipo_solicitud',
            'estado_expediente',
            'grupo_etario',
            'edad_persona',
            'situacion_habitacional_hist',
            'resumen_intervencion',
            'observaciones',
            'fecha_juzgado',
            'fecha_recepcion',
            'cuij',
            'clave_sisfe',
            'tipo_patrocinio',
            'expediente_fisico',
        ]
        labels = {
            'fecha_creacion': 'Fecha de creación',
            'sede': 'Sede',
            'institucion': 'Institución',
            'medio_ingreso': 'Medio de ingreso',
            'tipo_solicitud': 'Tipo de solicitud',
            'estado_expediente': 'Estado del expediente',
            'grupo_etario': 'Grupo etario',
            'edad_persona': 'Edad de la persona',
            'situacion_habitacional_hist': 'Situación Habitacional Histórica',
            'resumen_intervencion': 'Resumen de intervención',
            'observaciones': 'Observaciones',
            'fecha_juzgado': 'Fecha de juzgado',
            'fecha_recepcion': 'Fecha de recepción',
            'cuij': 'CUIJ',
            'clave_sisfe': 'Clave SISFE',
            'tipo_patrocinio': 'Tipo de patrocinio',
            'expediente_fisico': '¿Tiene expediente físico?',
        }
        widgets = {
            'fecha_creacion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_juzgado': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_recepcion': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'observaciones':
                field.widget.attrs.update({
                    'class': 'form-control custom-textarea',
                    'rows': 3,
                })
            elif name in ['expediente_fisico']:
                field.widget.attrs.update({
                    'class': 'form-check-input'
                })
            elif name in ['fecha_juzgado', 'fecha_recepcion', 'fecha_creacion']:
                field.widget.attrs.update({
                    'style': 'text-transform: uppercase;',
                })
            else:
                field.widget.attrs.update({
                    'class': 'form-control',
                    'style': 'text-transform: uppercase;',
                })



class ExpedienteOficioForm(forms.ModelForm):
    class Meta:
        model = ExpedienteOficio
        fields = [
            'fecha_creacion',
            'sede',
            'usuario_solicitante',
            'medio_ingreso',
            'tipo_solicitud',
            'estado_expediente',
            'grupo_etario',
            'edad_persona',
            'situacion_habitacional_hist',
            'resumen_intervencion',
            'observaciones',
            'fecha_juzgado',
            'fecha_recepcion',
            'cuij',
            'clave_sisfe',
            'tipo_patrocinio',
            'expediente_fisico',
        ]
        labels = {
            'fecha_creacion': 'Fecha de creación',
            'sede': 'Sede',
            'usuario_solicitante': 'Usuario solicitante',
            'medio_ingreso': 'Medio de ingreso',
            'tipo_solicitud': 'Tipo de solicitud',
            'estado_expediente': 'Estado del expediente',
            'grupo_etario': 'Grupo etario',
            'edad_persona': 'Edad de la persona',
            'situacion_habitacional_hist': 'Situación Habitacional Histórica',
            'resumen_intervencion': 'Resumen de intervención',
            'observaciones': 'Observaciones',
            'fecha_juzgado': 'Fecha de juzgado',
            'fecha_recepcion': 'Fecha de recepción',
            'cuij': 'CUIJ',
            'clave_sisfe': 'Clave SISFE',
            'tipo_patrocinio': 'Tipo de patrocinio',
            'expediente_fisico': '¿Tiene expediente físico?',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if name == 'observaciones':
                field.widget.attrs.update({
                    'class': 'form-control custom-textarea',
                    'rows': 3,
                })
            elif name == 'expediente_fisico':
                field.widget.attrs.update({
                    'class': 'form-check-input'
                })
            elif name in ['fecha_juzgado', 'fecha_recepcion', 'fecha_creacion']:
                field.widget.attrs.update({
                    'class': 'form-control',
                    'type': 'date',
                    'style': 'text-transform: uppercase;',
                })
            else:
                field.widget.attrs.update({
                    'class': 'form-control',
                    'style': 'text-transform: uppercase;',
                })
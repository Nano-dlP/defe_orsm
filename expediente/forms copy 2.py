from django import forms

from .models import ExpedienteDocumento, ExpedienteJudicial, ExpedientePresencial
from django.forms import modelformset_factory


class ExpedienteDocumentoForm(forms.ModelForm):
    class Meta:
        model = ExpedienteDocumento
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
ExpedienteDocumentoFormSet = modelformset_factory(
    ExpedienteDocumento,
    form=ExpedienteDocumentoForm,
    extra=2,         # cantidad de formularios vacíos a mostrar
    can_delete=True   # permite borrar documentos existentes
)


class ExpedientePresencialForm(forms.ModelForm):
    class Meta:
        model = ExpedientePresencial
        fields = [
            'fecha_ingreso',
            'medio_ingreso',
            'tipo_solicitud',
            'estado_expediente',
            'persona',
            'edad_persona',
            'grupo_etario',
            'sittuacion_habitacional',
            'resumen_intervencion',
            'observaciones',
        ]
        labels = {
            'fecha_ingreso': 'Fecha de ingreso',
            'medio_ingreso': 'Medio de ingreso',
            'tipo_solicitud': 'Tipo de solicitud',
            'estado_expediente': 'Estado del expediente',
            'persona': 'Persona',
            'edad_persona': 'Edad de la persona',
            'grupo_etario': 'Grupo etario',
            'sittuacion_habitacional': 'Situación Habitacional',
            'resumen_intervencion': 'Resumen de intervención',
            'observaciones': 'Observaciones',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplica Bootstrap 5 y mayúsculas excepto en 'observaciones'
        for name, field in self.fields.items():
            if name == 'observaciones':
                field.widget.attrs.update({
                    'class': 'form-control custom-textarea',
                    'rows': 2,
                    # NO aplicar text-transform aquí
                })
            else:
                field.widget.attrs.update({
                    'class': 'form-control',
                    'style': 'text-transform: uppercase;',
                })
        # Si tienes el campo 'identificador' en el modelo
        if 'identificador' in self.fields:
            self.fields['identificador'].widget.attrs.update({'readonly': 'readonly', 'class': 'form-control'})



class ExpedienteJudicialForm(forms.ModelForm):
    class Meta:
        model = ExpedienteJudicial
        fields = [
            'fecha_ingreso',
            'medio_ingreso',
            'institucion',
            'fecha_juzgado',
            'fecha_recepcion',
            'cuij',
            'clave_sisfe',
            'tipo_solicitud',
            'estado_expediente',
            'grupo_etario',
            'edad_persona',
            'situacion_habitacional',
            'resumen_intervencion',
            'observaciones',
            'situacion_habitacional_hist',
            'fecha_creacion',
            'fecha_de_juzgado',
            'fecha_de_recepcion',
        ]
        labels = {
            'fecha_ingreso': 'Fecha de ingreso',
            'medio_ingreso': 'Medio de ingreso',
            'institucion': 'Institución',
            'fecha_juzgado': 'Fecha de juzgado',
            'fecha_recepcion': 'Fecha de recepción',
            'cuij': 'CUIJ',
            'clave_sisfe': 'Clave SISFE',
            'tipo_solicitud': 'Tipo de solicitud',
            'estado_expediente': 'Estado del expediente',
            'grupo_etario': 'Grupo etario',
            'edad_persona': 'Edad de la persona',
            'situacion_habitacional': 'Situación Habitacional',
            'resumen_intervencion': 'Resumen de intervención',
            'observaciones': 'Observaciones',
            'situacion_habitacional_hist': 'Situación Habitacional Histórica',
            'fecha_creacion': 'Fecha de Creación',
            'fecha_de_juzgado': 'Fecha de Juzgado',
            'fecha_de_recepcion': 'Fecha de Recepción',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplica Bootstrap y Mayúsculas a todos menos observaciones
        for name, field in self.fields.items():
            if name == 'observaciones':
                field.widget.attrs.update({
                    'class': 'form-control custom-textarea',
                    'rows': 2,
                })
            elif name == 'situacion_habitacional_hist':
                field.widget.attrs.update({
                    'class': 'form-control',
                    'placeholder': 'Describir la situación habitacional histórica',
                    'style': 'text-transform: uppercase;',
                })
            elif name == 'fecha_creacion':
                field.widget.attrs.update({
                    'class': 'form-control',
                    'type': 'date',
                    'style': 'text-transform: uppercase;',
                })
            elif name == 'fecha_de_juzgado':
                field.widget.attrs.update({
                    'class': 'form-control',
                    'type': 'datetime-local',
                    'style': 'text-transform: uppercase;',
                })
            elif name == 'fecha_de_recepcion':
                field.widget.attrs.update({
                    'class': 'form-control',
                    'type': 'datetime-local',
                    'style': 'text-transform: uppercase;',
                })
            else:
                field.widget.attrs.update({
                    'class': 'form-control',
                    'style': 'text-transform: uppercase;',
                })
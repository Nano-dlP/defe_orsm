from django import forms

from .models import Expediente, ExpedienteDocumento
from django.forms import modelformset_factory


class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = '__all__'
        labels = {
            'numero': 'Número de expediente',
            'anio': 'Año del expediente',
            'abreviatura': 'Abreviatura',
            'fecha_creacion': 'Fecha de creación',
            'identificador': 'Identificador del expediente',
            'fecha_de_juzgado': 'Fecha del Juzgado',
            'fecha_de_recepcion': 'Fecha de Recepción',
            'cuij': 'CUIJ',
            'clave_sisfe': 'Clave SISFE',
            'estado_expediente': 'Estado del expediente',
            'sede': 'Sede',
            'medio_ingreso': 'Medio de ingreso',
            'expediente_fisico': 'Expediente físico',
            'tipo_solicitud': 'Tipo de solicitud',
            'tipo_patrocinio': 'Tipo de patrocinio',
            'resumen_intervencion': 'Resumen de intervención',
            'edad_persona': 'Edad de la persona',
            'grupo_etario': 'Grupo etario',
            'situacion_habitacional_hist': 'Situación habitacional histórica',
            'observaciones': 'Observaciones',
            'estado': 'Estado',
        }

    #La función se utiliza para darle estilo a los campos del formulario
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})
        # Modificar el estilo solo para 'observaciones'
        self.fields['observaciones'].widget.attrs.update({'class': 'form-control custom-textarea', 'rows': 2})
        # Modificar el estilo solo para 'situacion_habitacional_hist'
        self.fields['situacion_habitacional_hist'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Describir la situación habitacional histórica'})
        self.fields['fecha_creacion'].widget.attrs.update({'type': 'date'})
        self.fields['fecha_de_juzgado'].widget.attrs.update({'type': 'datetime-local'})
        self.fields['fecha_de_recepcion'].widget.attrs.update({'type': 'datetime-local'})

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



from django.contrib import admin

from .models import MotivoInternacion, MotivoAlta, ModalidadSuicidio, TipoAdiccion
# Register your models here.

admin.site.register(MotivoInternacion)
admin.site.register(MotivoAlta)
admin.site.register(ModalidadSuicidio)
admin.site.register(TipoAdiccion)

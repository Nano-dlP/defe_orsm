from django.db import models
from django.utils import timezone
from core.models import Sede
from persona.models import Persona
from institucion.models import Institucion
from usuario.models import CustomUser


# Create your models here.
class TipoSolicitud(models.Model):
    tipo_solicitud = models.CharField(max_length=50, verbose_name="Tipo de Solicitud")
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.tipo_solicitud
    
    class Meta:
        verbose_name = 'Tipo de solicitud'
        verbose_name_plural = 'Tipos de solicitudes'



class GrupoEtario(models.Model):
    grupo_etario = models.CharField(max_length=50, verbose_name="Grupo Etario")
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.grupo_etario
    
    class Meta:
        verbose_name = 'Grupo Etario'
        verbose_name_plural = 'Grupos etarios'


    
class ResumenIntervencion(models.Model):
    resumen_intervencion = models.CharField(max_length=50, verbose_name="Resumen de Intervención")
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.resumen_intervencion    
    
    class Meta:
        verbose_name = 'Resumen de Intervención'
        verbose_name_plural = 'Resumenes de intervenciones'


    
class TipoPatrocinio(models.Model):
    tipo_patrocinio = models.CharField(max_length=50, verbose_name="Tipo de Patrocinio")
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.tipo_patrocinio

    class Meta:
        verbose_name = 'Tipo de patrocinio'
        verbose_name_plural = 'Tipos de patrocinios'



class MedioIngreso(models.Model):
    medio_ingreso = models.CharField(max_length=50, verbose_name="Medio de Ingreso")
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.medio_ingreso
    
    class Meta:
        verbose_name = 'Medio de Ingreso'
        verbose_name_plural = 'Medios de Ingresos'



class EstadoExpediente(models.Model):
    estado_expediente = models.CharField(max_length=100, verbose_name="Estado el expediente")
    estado = models.BooleanField(default=True)
    
    def __str__(self):
        return self.estado_expediente
    
    class Meta:
        verbose_name = 'Estado del expediente'
        verbose_name_plural = 'Estado de los expedientes'
        


class Rol (models.Model):
    rol = models.CharField('Rol', max_length=50, blank=True, null=True)
    
    def __str__(self):
        return self.rol
    
    class Meta:
        verbose_name = 'Rol'
        verbose_name_plural = 'Roles'



class ExpedientePresencialDocumento(models.Model):
    expediente = models.ForeignKey('ExpedientePresencial', on_delete=models.CASCADE, related_name='documentos')
    nombre = models.CharField("Nombre del documento", max_length=255, blank=True, null=True)
    archivo = models.FileField(upload_to='documentos/presencial/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre or 'Documento'}"


class ExpedienteJudicialDocumento(models.Model):
    expediente = models.ForeignKey('ExpedienteJudicial', on_delete=models.CASCADE, related_name='documentos')
    nombre = models.CharField("Nombre del documento", max_length=255, blank=True, null=True)
    archivo = models.FileField(upload_to='documentos/judicial/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre or 'Documento'}"
    

class ExpedienteOficioDocumento(models.Model):
    expediente = models.ForeignKey('ExpedienteOficio', on_delete=models.CASCADE, related_name='documentos')
    nombre = models.CharField("Nombre del documento", max_length=255, blank=True, null=True)
    archivo = models.FileField(upload_to='documentos/oficio/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre or 'Documento'}"
    


class ExpedienteBase(models.Model):
    numero = models.PositiveIntegerField("Número de expediente")
    anio = models.PositiveIntegerField("Año del expediente", default=2025)
    abreviatura = models.CharField("Abreviatura", max_length=4)
    fecha_creacion = models.DateField("Fecha de creación", auto_now_add=False)
    identificador = models.CharField("Identificador del expediente", max_length=100, unique=True, editable=False)
    
    sede = models.ForeignKey(Sede, on_delete=models.PROTECT, verbose_name='Sede')
    medio_ingreso = models.ForeignKey('MedioIngreso', on_delete=models.CASCADE, blank=True, null=True)
    tipo_solicitud = models.ForeignKey('TipoSolicitud', on_delete=models.CASCADE)
    estado_expediente = models.ForeignKey('EstadoExpediente', on_delete=models.CASCADE)
    grupo_etario = models.ForeignKey('GrupoEtario', on_delete=models.CASCADE)
    edad_persona = models.PositiveIntegerField(blank=True, null=True)
    situacion_habitacional_hist = models.CharField(verbose_name= 'Situación habitacional historica', max_length=255, blank=True, null=True)
    resumen_intervencion = models.ForeignKey('ResumenIntervencion', on_delete=models.CASCADE, blank=True, null=True)
    observaciones = models.TextField(verbose_name='Observaviones', blank=True, null=True)

    class Meta:
        abstract = True  # <--- Esto es importante
        ordering = ['-anio', '-numero']

    def save(self, *args, **kwargs):
        if not self.pk:
            today = timezone.now().date()
            self.anio = today.year
            if not self.abreviatura and self.sede:
                self.abreviatura = self.sede.abreviatura.upper()
            ultimo = self.__class__.objects.filter(
                sede=self.sede,
                anio=self.anio
            ).order_by('-numero').first()
            self.numero = (ultimo.numero + 1) if ultimo else 1
            self.identificador = f"{self.abreviatura}-{str(self.numero).zfill(5)}-{self.anio}"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.identificador
    



class ExpedientePresencial(ExpedienteBase):
    grupo_etario = models.ForeignKey('GrupoEtario', related_name='presencial_grupo_etario', on_delete=models.CASCADE)
    estado_expediente = models.ForeignKey('EstadoExpediente', related_name='presencial_estado_expediente', on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return f"Expediente Presencial: {self.identificador} - {self.persona}"
    


class ExpedienteJudicial(ExpedienteBase):
    grupo_etario = models.ForeignKey('GrupoEtario', related_name='judicial_grupo_etario', on_delete=models.CASCADE)
    estado_expediente = models.ForeignKey('EstadoExpediente', related_name='judicial_estado_expediente', on_delete=models.CASCADE)
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE)
    fecha_juzgado = models.DateField("Fecha en que el juzgado toma conocimiento", blank=True, null=True)
    fecha_recepcion = models.DateField("Fecha de recepción del expediente judicial", blank=True, null=True)
    cuij = models.CharField("CUIJ", max_length=100, blank=True, null=True)
    clave_sisfe = models.CharField("Clave SISFE", max_length=100, blank=True, null=True)
    tipo_patrocinio = models.ForeignKey('TipoPatrocinio', on_delete=models.CASCADE, blank=True, null=True)
    expediente_fisico = models.BooleanField("¿Tiene expediente físico?", default=False)

    def __str__(self):
        return f"Expediente Judicial: {self.identificador} - {self.institucion}"
    


class ExpedienteOficio(ExpedienteBase):
    grupo_etario = models.ForeignKey('GrupoEtario', related_name='oficio_grupo_etario', on_delete=models.CASCADE)
    estado_expediente = models.ForeignKey('EstadoExpediente', related_name='oficio_estado_expediente', on_delete=models.CASCADE)
    usuario_solicitante = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='expedienteoficio_usuario_solicitante')
    fecha_juzgado = models.DateField("Fecha en que el juzgado toma conocimiento", blank=True, null=True)
    fecha_recepcion = models.DateField("Fecha de recepción del expediente judicial", blank=True, null=True)
    cuij = models.CharField("CUIJ", max_length=100, blank=True, null=True)
    clave_sisfe = models.CharField("Clave SISFE", max_length=100, blank=True, null=True)
    tipo_patrocinio = models.ForeignKey('TipoPatrocinio', on_delete=models.CASCADE, blank=True, null=True)
    expediente_fisico = models.BooleanField("¿Tiene expediente físico?", default=False)

    def __str__(self):
        return f"Expediente Oficio: {self.identificador} - {self.usuario_solicitante}"



class ExpedientePersona(models.Model):
    expediente = models.ForeignKey(ExpedientePresencial, on_delete=models.CASCADE, related_name='expedientepresencial_expediente')
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='expedientepresencial_persona')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='expedientepresencial_rol')



class ExpedienteInstitucion(models.Model):
    expediente = models.ForeignKey(ExpedienteJudicial, on_delete=models.CASCADE, related_name='expedientejudicial_expediente')
    institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, related_name='expedientejudicial_institucion')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='expedientejudicial_rol')



class ExpedienteOficioso(models.Model):
    expediente = models.ForeignKey(ExpedienteOficio, on_delete=models.CASCADE, related_name='expedienteoficioso_expediente')
    usuario_solicitante = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='expedienteoficioso_usuario_solicitante')
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, related_name='expedienteoficioso_rol')





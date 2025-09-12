from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    #path('', include('institucion.urls')),
    path('', include('persona.urls')),
    #path('', include('expediente.urls')),
    #path('', include('usuario.urls')),
    #path('', include('profesional.urls')),
    #path('', include('internacion.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
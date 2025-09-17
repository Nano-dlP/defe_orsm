# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import TemplateView



class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'core/index.html'
    login_url = 'core:login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Bienvenido a DEFE-ORSM'
        return context


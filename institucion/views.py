from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import CreateView
from .models import Institucion
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.contrib import messages

from django.http import HttpResponseRedirect

from .forms import InstitucionForm



class InstitucionCreateView(LoginRequiredMixin, CreateView):
    model = Institucion
    template_name = 'institucion/institucion_crear.html'
    form_class = InstitucionForm
    success_url = reverse_lazy('core:index')
    context_object_name = 'institucion'
    login_url = 'core:login'

    
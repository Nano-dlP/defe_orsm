from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView

from .views import  IndexView

app_name = 'core'

urlpatterns = [
    
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='core:index'), name='logout'),


]

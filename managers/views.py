from django.shortcuts import render

from django.shortcuts import render
from django.views.generic import ListView
from managers.models import Managers



class ManagersView(ListView):
    template_name = 'managers.html'
    model = Managers
    context_object_name = 'managers'
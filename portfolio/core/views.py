from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) #first, call super get context date
        context['about'] = About.objects.first()
        context['services'] = Service.objects.first()
        context['works'] = RecentWork.objects.first()
        return context

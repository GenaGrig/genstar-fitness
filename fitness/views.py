from django.shortcuts import render, get_object_or_404
from django.views import generic


class MainPageView(generic.TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Genstar'
        return context
    
    


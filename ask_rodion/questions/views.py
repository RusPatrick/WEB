from django.shortcuts import render
from django.views.generic import TemplateView

def post_list(request):
    return render(request, 'base.html', {})

class BaseView(TemplateView):
    template_name = "base.html"

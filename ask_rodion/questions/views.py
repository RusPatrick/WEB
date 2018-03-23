from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils import timezone
from .models import Question

def post_list(request):
    questions = Question.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'index.html', {'questions': questions})

class BaseView(TemplateView):
    template_name = "base.html"

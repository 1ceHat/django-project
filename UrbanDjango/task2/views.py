from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


def func_views(request):
    return render(request, 'func_template.html')


class ClassViews(TemplateView):
    template_name = 'class_template.html'

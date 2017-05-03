from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse


def index(request):
    template = loader.get_template('home/home.html')
    context = {
        'output': "Hello, world. You're at the polls index.",
    }
    return HttpResponse(template.render(context, request))
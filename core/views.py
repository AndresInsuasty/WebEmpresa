from django.shortcuts import render, HttpResponse
# Create your views here.


def home(request):
    return HttpResponse('Inicio home/')

def about(request):
    return HttpResponse('Historia about/')

def services(request):
    return HttpResponse('Servicios services/')

def store(request):
    return HttpResponse('Visítanos store/')

def contact(request):
    return HttpResponse('Contacto contact/')

def blog(request):
    return HttpResponse('Blog blog/')

def sample(request):
    return HttpResponse('Sample sample/')
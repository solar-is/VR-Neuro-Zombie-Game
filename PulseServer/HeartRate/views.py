from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from HeartRate.models import PulseValue


def create(request):
    PulseValue.objects.create()
    return HttpResponse('Cell created successfully')


def update(request):
    pulse_cell = list(PulseValue.objects.all())[-1]
    pulse_cell.value = request.GET['bpm']
    pulse_cell.save()
    return HttpResponse('Value Updated')


def get(request):
    pulse_cell = list(PulseValue.objects.all())[-1]

    response = HttpResponse('{}'.format(pulse_cell.value))
    #response.headers['bpm'] = pulse_cell.value
    return response

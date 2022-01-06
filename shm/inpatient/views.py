from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inpatients(request):
    return HttpResponse('Inpatient page')
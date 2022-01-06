from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def new_patient(request):
    return HttpResponse('This is the patients page')
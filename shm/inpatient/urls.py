from django.urls import path
from . import views

urlpatterns = [
    path('', views.inpatients, name='inpatients')
]

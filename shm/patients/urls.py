from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_patient, name='new_patient')

]

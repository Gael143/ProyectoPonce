from django.urls import path
from . import views
from .views import registro_paciente, agenda_cita, detalles_cita, proceder_pago

urlpatterns = [
    path('', views.home),
    path('registro_paciente/', registro_paciente, name='registro_paciente'),
    path('agenda_cita/', agenda_cita, name='agenda_cita'),
    path('detalles_cita/<int:cita_id>/', detalles_cita, name='detalles_cita'),
    path('proceder_pago/<int:cita_id>/', proceder_pago, name='proceder_pago'),
]



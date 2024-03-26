from django import forms
from .models import Paciente, Cita

class RegistroPacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'edad', 'direccion', 'telefono', 'correo']


class AgendaCitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente', 'fecha', 'hora', 'duracion', 'motivo']


from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente
from .forms import RegistroPacienteForm, AgendaCitaForm
from .models import Cita

# Create your views here.
def home(request):
    return render(request, "registroPacientes.html")

def registro_paciente(request):
    if request.method == 'POST':
        form = RegistroPacienteForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('agenda_cita')  
           
    else:
        form = RegistroPacienteForm()

    return render(request, 'registroPacientes.html', {'form': form})


def agenda_cita(request):
    if request.method == 'POST':
        form = AgendaCitaForm(request.POST)
        if form.is_valid():
            cita = form.save()
            
            return redirect('detalles_cita', cita_id=cita.id)
    else:
        form = AgendaCitaForm()
    
    return render(request, 'agendaCitas.html', {'form': form})


def detalles_cita(request, cita_id):
    cita = Cita.objects.get(id=cita_id)
    return render(request, 'detallesCita.html', {'cita': cita})

def proceder_pago(request, cita_id):
    cita = get_object_or_404(Cita, pk=cita_id)
    return render(request, 'pago.html', {'cita': cita})



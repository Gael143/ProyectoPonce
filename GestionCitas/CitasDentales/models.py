from django.db import models

# Create your models here.

class Paciente(models.Model):
    nombre = models.CharField(max_length=255)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora = models.TimeField()
    duracion = models.PositiveIntegerField()  # Suponiendo que la duración se mide en minutos
    motivo = models.TextField()

    def __str__(self):
        return f"{self.paciente.nombre} - {self.fecha} {self.hora}"
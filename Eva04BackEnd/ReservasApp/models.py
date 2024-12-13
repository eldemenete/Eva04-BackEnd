from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Reserva(models.Model):
    Estado = (
        ('RESERVADO', 'Reservado'),
        ('COMPLETADA', 'Completada'),
        ('ANULADA', 'Anulada'),
        ('NO ASISTEN', 'No Asisten'),
    )

    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    fecha_reserva = models.DateField()
    hora_reserva = models.TimeField()
    cantidad_personas = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(15)])
    estado = models.CharField(max_length=10, choices=Estado, default='RESERVADO')
    observaciones = models.TextField(blank=True, null=True)  # Asegúrate de que esté correctamente definido

    def __str__(self):
        return f"Reserva de {self.nombre} para {self.cantidad_personas} personas"
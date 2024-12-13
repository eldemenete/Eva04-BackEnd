from rest_framework import serializers
from .models import Reserva

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id', 'nombre', 'telefono', 'fecha_reserva', 'hora_reserva', 'cantidad_personas', 'estado', 'observacion']

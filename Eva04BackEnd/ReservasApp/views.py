from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Reserva
from .serializers import ReservaSerializer
from rest_framework import generics

def lista_reservas(request):
    reservas = Reserva.objects.all()
    return render(request, 'ReservasApp/lista_reservas.html', {'reservas': reservas})

class ReservaList(generics.ListCreateAPIView):
    queryset = Reserva.objects.all().order_by('fecha_reserva')
    serializer_class = ReservaSerializer

# Vista para obtener, actualizar o eliminar una reserva en particular
class ReservaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

def index(request):
    return render(request, 'ReservasApp/index.html')
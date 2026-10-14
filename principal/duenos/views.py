from rest_framework import viewsets
from .models import Dueno
from .serializers import DuenoSerializer

class DuenoViewSet(viewsets.ModelViewSet):
    queryset = Dueno.objects.all()
    serializer_class = DuenoSerializer

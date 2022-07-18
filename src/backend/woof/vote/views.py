from django.shortcuts import render
from rest_framework import generics

from .models import Ballots
from .serializers import BallotsSerializer

# Create your views here.
class BallotsView(generics.ListAPIView):
    queryset = Ballots.objects.all()
    serializer_class = BallotsSerializer

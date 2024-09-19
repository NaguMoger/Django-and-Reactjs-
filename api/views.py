from django.shortcuts import render
from rest_framework import generics
from .models import Students
from .serializer import StudentSerializer

# Create your views here.

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
    
class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
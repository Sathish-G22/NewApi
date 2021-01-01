from django.shortcuts import render

# Create your views here.
from .models import student
from .serializers import studentSerializer
from rest_framework import viewsets



class studentViewsets(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=studentSerializer

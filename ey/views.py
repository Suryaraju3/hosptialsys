# from django.shortcuts import render
from rest_framework import generics
from .serializes import DoctorSerializer,PatientSerializer,PharmacySerializer,userSerializer
from .models import PatientDetails,Doctors,Pharmacy
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view



class DoctorList(generics.ListCreateAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer


class DotorsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

class PatientList(generics.ListCreateAPIView):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientSerializer
    
class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientSerializer
    permission_classes =  [IsAuthenticated] 

class PharmacyList(generics.ListCreateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer

class PharmacyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pharmacy.objects.all()
    permission_classes = [IsAuthenticated]
    
class Usercreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer
    

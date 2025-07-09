# from django.shortcuts import render
from rest_framework import generics
from .serializes import DoctorSerializers,PatientSerializer,PharmacySerializer,userSerializer
from .models import PatientDetails,Doctors,Pharmacy
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework.permissions import IsAuthenticated

class DoctorList(generics.ListCreateAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializers
    
class PatientList(generics.ListCreateAPIView):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientSerializer

class PharmacyList(generics.ListCreateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    
    
class PatientDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientSerializer
    permission_classes =  [IsAuthenticated]  
 
    
class Usercreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer
    serializer_class = []
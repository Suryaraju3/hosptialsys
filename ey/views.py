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
from rest_framework import status
from rest_framework.decorators import api_view

class DoctorList(generics.ListCreateAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer
    
def doctor(request):
    if request.method == 'POST':
        doctor = Doctors.objects.all()
        serializer = DoctorSerializer(doctor,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    
    
class PatientList(generics.ListCreateAPIView):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientSerializer

class PharmacyList(generics.ListCreateAPIView):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer

    
class PatientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PatientDetails.objects.all()
    serializer_class = PatientSerializer
    permission_classes =  [IsAuthenticated] 
    
@api_view(['GET','POST'])  
def patientDetail(request):
    if request.method == 'GET':
        patient =PatientDetails.objects.all()
        serializer = PatientSerializer(patient,many=True)
        return Response (serializer.data)
    elif request.method == 'POST':
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['DELETE'])
def del_pdetails(request,pk):
    try:
        patient = patientDetail.objects.get(pk=pk)
        patient.delete()
        return Response({"Message": "Deleted"})
    except patientDetail.DoesNotExist:
        return Response({"Error":"Not Found"}, status=404)
    
     
    
class DotorsDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctors.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]

class PharmacyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pharmacy.objects.all()
    permission_classes = [IsAuthenticated]

@api_view(['GET','POST'])
def pharmacy_view(request):
    if request.method == "GET":
        phar = Pharmacy.objects.all()
        serializer = PharmacySerializer(phar, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PharmacySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    
class Usercreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer
    serializer_class = []
    
class LoginView(APIView):
    def post(self, request):
        
        username = request.data.get("username")
        password = request.data.get("password")
        
        user = authenticate(username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            
            response = Response({
                'access': str(refresh.access_token),
                'user': user.username,}, status=status.HTTP_200_OK)

            response.set_cookie(
                key='refresh_token',
                value=str(refresh),
                httponly=True,
                secure=False,  
                samesite='Lax',
                path='/',
            )
            return response
        return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
  

        
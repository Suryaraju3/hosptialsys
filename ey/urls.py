from django.urls import path
from .views import DoctorList,PatientList,PharmacyList
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    
    
    path('token/',TokenObtainPairView.as_view(),name='token'),
    path('refresh/',TokenRefreshView.as_view(),name='refresh'),
    path('doctor/', DoctorList.as_view(),name='d-details'),
    path('pdetails/',PatientList.as_view(),name="p-details"),
    path('phcy/',PharmacyList.as_view(),name="ph-details"),
    
]

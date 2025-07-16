from django.urls import path
from .views import DoctorList,PatientList,PharmacyList,PatientDetail,DotorsDetails,PharmacyDetails,LoginView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    
        
    path('token/',TokenObtainPairView.as_view(),name='token'),
    path('token/refresh/',TokenRefreshView.as_view(),name='refresh'),
    path('pdetails/',PatientList.as_view(),name="p-list"),
    path('pdetail/<int:pk>/',PatientDetail.as_view(),name="p-details"),
    path('doctor/', DoctorList.as_view(),name='d-details'),
    path('doctor/<int:pk>/',DotorsDetails.as_view(),name='d-detail'),
    path('phcy/<int:pk>/',PharmacyDetails.as_view(),name='phar-details'),
    path('phcy/',PharmacyList.as_view(),name="ph-details"), 
    path('login/',LoginView.as_view(),name='Login'),
]


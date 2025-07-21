from django.urls import path
from .views import DoctorList,PatientList,PharmacyList,PatientDetail,DotorsDetails,PharmacyDetails,Usercreate
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('user/',Usercreate.as_view(),name='user-create'),
    path('token/',TokenObtainPairView.as_view(),name='token'),
    path('token/refresh/',TokenRefreshView.as_view(),name='refresh'),
    path('pdetails/',PatientList.as_view(),name="p-list"),
    path('pdetails/<int:pk>/',PatientDetail.as_view(),name="p-details"),
    path('doctors/', DoctorList.as_view(),name='d-details'),
    path('doctors/<int:pk>/',DotorsDetails.as_view(),name='d-detail'),
    path('pharmacy/<int:pk>/',PharmacyDetails.as_view(),name='phar-details'),
    path('pharmacy/',PharmacyList.as_view(),name="ph-details"), 
    
]


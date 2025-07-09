from django.contrib import admin

from .models import PatientDetails,Doctors,Pharmacy

admin.site.register(PatientDetails)
admin.site.register(Doctors)
admin.site.register(Pharmacy)

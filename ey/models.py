from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

    
class Doctors(models.Model):
    Did=models.AutoField(primary_key=True)
    DoctorName=models.CharField(max_length=100)
    specialist=models.CharField(max_length=200)
    Block=models.CharField(max_length=100)
    Roomno=models.IntegerField()

    def __str__(self):
        return self.DoctorName
    
class PatientDetails(models.Model):
    Pid=models.AutoField(primary_key=True)
    Name=models.CharField(max_length=150)
    Age=models.IntegerField()
    Sex=models.CharField(max_length=20)
    Dateorbirth=models.DateField()
    Phonenumber=PhoneNumberField()
    Address=models.TextField()
    Date=models.DateTimeField(auto_now=True)
    Issue=models.TextField()
    DoctorName=models.CharField(max_length=100)
    Did=models.ForeignKey(Doctors, on_delete=models.CASCADE)
    Block=models.CharField(max_length=100)
    Roomno=models.IntegerField()
    
    
    def __str__(self):
        return self.Name
    
class Pharmacy(models.Model):
    pharmacyid=models.AutoField(primary_key=True)
    Pid=models.ForeignKey(PatientDetails,on_delete=models.CASCADE)
    DoctorName=models.CharField(max_length=100)
    Name=models.CharField(max_length=150)
    Age=models.IntegerField()
    Sex=models.CharField(max_length=20)
    Description=models.TextField()
    Qty=models.IntegerField()
    Total=models.DecimalField(max_digits=8,decimal_places=2)
    
    
    def __str__(self):
        return self.pharmacyid
    
    
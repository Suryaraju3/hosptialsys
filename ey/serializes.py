from rest_framework import serializers
from .models import PatientDetails,Doctors,Pharmacy
from django.contrib.auth.models import User

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientDetails
        fields ='__all__'
   
       
class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [ 'username','password','email']
    def create(self,validated_data):
        user = User.objects.create_user(username=validated_data['username'],
                                        password=validated_data['password'],
                                        email=validated_data.get('email',''))
        return user
from rest_framework import serializers
from .models import Patient,LabResult,Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'provider', 'date_time', 'location', 'reason', 'notes']


class PatientSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(error_messages={'invalid': 'Enter a valid email address.'})

    phone = serializers.IntegerField(min_value=10000000, max_value=99999999,
     error_messages={'min_value': 'Phone number must be at least 8 digits long.',
      'max_value': 'Phone number must be no more than 8 digits long.'})

    class Meta:
        model = Patient
        fields = ["id","full_name", "phone", "email","dob"]
        # fields = ["full_name", "phone", "email","dob","gender","address","emergency_contact_phone"]

    def create(self, validated_data):
        phone = validated_data['phone']
        try:
            patient = Patient.objects.get(phone=phone)
            raise serializers.ValidationError({'phone': 'Patient with this Phone already exists.'})
        except Patient.DoesNotExist:
            pass
        return super().create(validated_data)    

class LabResultSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = LabResult
        fields = ['id', 'patient', 'test_name','test_date','test_result']
      


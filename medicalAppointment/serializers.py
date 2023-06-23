from rest_framework import serializers
from medicalAppointment.models import MedicalAppointment, StatusFieldChoices
from registry.serializers import DoctorSerializer, PatientSerializer


class MedicalAppointmentSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(choices=StatusFieldChoices.choices, required=False)

    class Meta:
        doctor = DoctorSerializer()
        patient = PatientSerializer()
        model = MedicalAppointment
        fields = ["id", "doctor", "patient", "description", "appointmentDate", "status"]
        read_only_fields = ["id"]

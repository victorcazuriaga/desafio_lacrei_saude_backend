from rest_framework import serializers
from .models import Address, Doctor, Patient


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
        read_only_field = ["id"]


class DoctorSerializer(serializers.ModelSerializer):
    address = AddressSerializer()
    socialName = serializers.CharField(required=False)
    comments = serializers.CharField(required=False)

    class Meta:
        model = Doctor
        fields = [
            "id",
            "socialName",
            "name",
            "lastName",
            "email",
            "cpf",
            "rg",
            "crm",
            "medicalSpecialty",
            "birthdate",
            "is_active",
            "address",
            "comments",
        ]
        read_only_field = ["id"]

    def create(self, validated_data):
        address_data = validated_data.pop("address")
        new_address = Address.objects.create(**address_data)
        new_doctor = Doctor.objects.create(**validated_data, address=new_address)
        return new_doctor


class PatientSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True)
    socialName = serializers.CharField(required=False)
    comments = serializers.CharField(required=False)

    class Meta:
        model = Patient
        fields = [
            "id",
            "socialName",
            "name",
            "lastName",
            "email",
            "cpf",
            "rg",
            "birthdate",
            "is_active",
            "address",
            "comments",
        ]

        read_only_field = ["id", "is_active"]

        def create(self, validated_data):
            address_data = validated_data.pop("address")
            new_address = Address.objects.create(**address_data)
            new_patient = Patient.objects.create(**validated_data, address=new_address)
            return new_patient

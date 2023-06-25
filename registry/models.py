import uuid
from django.db import models


# Create your models here.

class Address(models.Model): 
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    zipcode = models.CharField(max_length=8)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=100)
    street = models.CharField(max_length=200)
    number = models.CharField(max_length=10)

class Doctor(models.Model):
   id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
   socialName = models.CharField(max_length=124, blank= True)
   name = models.CharField(max_length=64)
   lastName = models.CharField(max_length=64)
   email = models.CharField(max_length=64, unique = True)
   cpf = models.CharField(max_length=11, unique=True)
   rg = models.CharField(max_length=7, unique=True)
   crm = models.CharField(max_length=10, unique=True)
   medicalSpecialty = models.CharField(max_length=64)
   birthdate = models.DateField()
   is_active = models.BooleanField(default=True)
   address = models.OneToOneField("Address", on_delete=models.CASCADE, null=True, blank=True)
   comments  = models.CharField(max_length=124)
#    medicalAppointment = models.
   def __str__(self) -> str:
                return f"{self.name}, {self.lastName}, ({self.crm})"
   
   def delete(self, using=None, keep_parents=False):
        if self.address:
            self.address.delete()
        super().delete(using, keep_parents)       



class Patient(models.Model):
   id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
   socialName = models.CharField(max_length=124, blank= True)
   name = models.CharField(max_length=64)
   lastName = models.CharField(max_length=64)
   email = models.CharField(max_length=64,unique=True)
   cpf = models.CharField(max_length=11,unique=True)
   rg = models.CharField(max_length=7, unique=True)
   birthdate = models.DateField()
   is_active = models.BooleanField(default=True)
   address = models.OneToOneField(Address, on_delete=models.CASCADE,  null=True, blank=True)
   comments  = models.CharField(max_length=124)
#    medicalAppointment = models.
   def delete(self, using=None, keep_parents=False):
        if self.address:
            self.address.delete()
        super().delete(using, keep_parents)       

   def __str__(self) -> str:
        return f"{self.name}, {self.lastName}, {self.cpf}"


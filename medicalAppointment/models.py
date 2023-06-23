import uuid
from django.db import models
from registry.models import Doctor, Patient


class StatusFieldChoices(models.TextChoices):
    AGENDADO = "AGENDADO", "Agendado"
    CANCELADO = "CANCELADO", "CANCELADO"
    CONCLUIDO = "CONCLUIDO", "CONCLUIDO"


# Create your models here.
class MedicalAppointment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    appointmentDate = models.DateTimeField()
    last_modified = models.DateTimeField(
        auto_now=True,
    )
    status = models.CharField(
        max_length=34,
        choices=StatusFieldChoices.choices,
        default=StatusFieldChoices.AGENDADO,
    )
    description = models.TextField()

from django.db import models

# Create your models here.

class LegalAidProvider(models.Model):
    PROVIDER_TYPES = (
        ('lawyer', 'Lawyer'),
        ('organization', 'Organization'),
    )
    name = models.CharField(max_length=200)
    provider_type = models.CharField(max_length=20, choices=PROVIDER_TYPES)
    contact_info = models.TextField()
    specialties = models.CharField(max_length=200)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.provider_type})"

class Service(models.Model):
    provider = models.ForeignKey(LegalAidProvider, on_delete=models.CASCADE, related_name='services')
    description = models.TextField()
    service_type = models.CharField(max_length=100)  # E.g., "Consultation", "Representation"

    def __str__(self):
        return f"{self.service_type} - {self.provider.name}"
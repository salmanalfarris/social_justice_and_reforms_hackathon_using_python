from django.db import models
from django.contrib.auth import get_user_model
from legal_aid.models import LegalAidProvider
# Create your models here.

User = get_user_model()

class CourtCase(models.Model):
    STATUS_CHOICES = (
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('closed', 'Closed'),
    )
    case_number = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cases')
    assigned_lawyer = models.ForeignKey(LegalAidProvider, on_delete=models.SET_NULL, null=True, blank=True, related_name='cases')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    start_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.case_number})"

class CaseUpdate(models.Model):
    court_case = models.ForeignKey(CourtCase, on_delete=models.CASCADE, related_name='updates')
    update_text = models.TextField()
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Update for {self.court_case.title} on {self.update_date}"
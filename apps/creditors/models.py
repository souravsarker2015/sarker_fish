from django.db import models

from apps.core.models import BaseModel

CREDITOR_TYPE_CHOICES = [
    ('bank', 'Bank'),
    ('individual', 'Individual'),
    ('corporation', 'Corporation'),
    ('shop', 'Shop'),
]


class Creditor(BaseModel):
    creditor_name = models.CharField(max_length=255)
    creditor_type = models.CharField(max_length=30, choices=CREDITOR_TYPE_CHOICES)
    credit_amount = models.DecimalField(max_digits=10, decimal_places=2)

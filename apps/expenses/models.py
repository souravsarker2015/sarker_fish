from django.db import models

from apps.core.models import BaseModel

EXPENSE_TYPE_CHOICES = [
    ('bank', 'Bank'),
    ('individual', 'Individual'),
    ('corporation', 'Corporation'),
    ('shop', 'Shop'),
    ('family', 'Family'),
]


class Expense(BaseModel):
    expense_date = models.DateField()
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_type = models.CharField(max_length=30, choices=EXPENSE_TYPE_CHOICES)
    expense_details = models.TextField()

from django.db import models

from apps.core.models import BaseModel
from apps.ponds.models import Pond

EXPENSE_TYPE_CHOICES = [
    ('bank', 'Bank'),
    ('individual', 'Individual'),
    ('corporation', 'Corporation'),
    ('shop', 'Shop'),
    ('family', 'Family'),
    ('pond', 'Pond'),
]


class Expense(BaseModel):
    expense_date = models.DateField()
    expense_amount = models.DecimalField(max_digits=10, decimal_places=2)
    expense_type = models.CharField(max_length=30, choices=EXPENSE_TYPE_CHOICES)
    pond = models.ForeignKey(Pond, on_delete=models.CASCADE, null=True, blank=True)
    expense_details = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'expense'

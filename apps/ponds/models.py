from django.db import models

from apps.core.models import BaseModel


class Pond(BaseModel):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'ponds'

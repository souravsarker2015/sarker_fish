from django.db import models

from apps.core.models import BaseModel


class Pond(BaseModel):
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'ponds'

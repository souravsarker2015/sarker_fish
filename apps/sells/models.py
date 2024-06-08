from apps.core.models import BaseModel

from django.db import models


class Sell(BaseModel):
    sell_date = models.DateField()
    sell_price = models.DecimalField(max_digits=10, decimal_places=2)
    sell_image = models.ImageField(upload_to='sell_images', null=True, blank=True)
    sell_place = models.CharField(max_length=254, null=True, blank=True)
    buyer = models.CharField(max_length=254, null=True, blank=True)
    sell_description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'sell'

from django import forms

from apps.sells.models import Sell


class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = ['sell_date', 'sell_price', 'sell_image', 'sell_place', 'buyer', 'sell_description']

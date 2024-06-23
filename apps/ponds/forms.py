from django import forms

from apps.ponds.models import Pond


class PondForm(forms.ModelForm):
    class Meta:
        model = Pond
        fields = ['name', 'location']

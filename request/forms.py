
from django import forms

from request.models import Rerust


class RerustForm(forms.ModelForm):
    class Meta:
        model = Rerust
        fields = ['name', 'email', 'question', 'id_manager', 'object_link']

    id_manager = forms.IntegerField(widget=forms.HiddenInput)



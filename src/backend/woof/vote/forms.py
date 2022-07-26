from .models import Ballots
from django import forms


class BallotsForm(forms.ModelForm):
    class Meta:
        model = Ballots
        fields = ("id", "dog_vote", "cat_vote", "voted_at")

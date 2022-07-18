from rest_framework import serializers
from .models import Ballots


class BallotsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ballots
        fields = ("id", "dog_vote", "cat_vote", "voted_at")

from django.db import models

# Create your models here.
class Ballots(models.Model):
    dog_vote = models.BooleanField(blank=True, default=False)
    cat_vote = models.BooleanField(blank=True, default=False)
    voted_at = models.DateTimeField(auto_now_add=True)

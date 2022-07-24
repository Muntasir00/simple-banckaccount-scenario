from gc import freeze
from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=30)
    balance = models.IntegerField()
    freeze_type = models.BooleanField(default=False)
    hold = models.BooleanField(default=False)

    def __str__(self):
        return self.username

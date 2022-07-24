from rest_framework import viewsets
from . import models 
from . import serializers

class AccountViewset(viewsets.ModelViewSet):
    querset =models.Account.objects.all()
    serializer_class = serializers.AccountSerializer
from pyexpat import model
from rest_framework import serializers
from .models import Account

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__' 

class transferSerializer(serializers.Serializer):
    from_account = serializers.IntegerField()
    to_account = serializers.IntegerField()
    balance = serializers.IntegerField()
    # class Meta:
    #     model = Account
    #     fields = fields = ('__all__')




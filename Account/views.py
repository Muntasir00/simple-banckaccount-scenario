from django.http import JsonResponse
from django.shortcuts import render
from .models import Account
import random
from Account import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AccountSerializer, AccountCreateSerializer



# Create your views here.
def home(request):
    accounts = Account.objects.all()
    return render(request,'home.html',{'accounts':accounts})

def create(request):
    n=random.randint(50,500)
    charsCU = list('ACDEFGHIJKLMNOPQRSTWXYZ')
    charscs = list('abcdefghijklmnopqrstwxyz')
    name = ""
    for x in range(1):
        name += random.choice(charsCU)
    for x in range(10):
        name += random.choice(charscs)
    name += " "
    for x in range(1):
        name += random.choice(charsCU)
    for x in range(6):
        name += random.choice(charscs)

    b = Account(username=name, balance=n)
    b.save()
    accounts = Account.objects.all()
    return render(request,'home.html',{'accounts':accounts})


def transfer(request):
    from_account_id =  int(request.GET.get('from_account'))
    to_account_id =  int(request.GET.get('to_account'))
    transfer_amount = int(request.GET.get('amount'))

    from_account = Account.objects.get(id=from_account_id)
    to_account = Account.objects.get(id=to_account_id)

    from_account.balance = from_account.balance - transfer_amount
    to_account.balance = to_account.balance + transfer_amount
    from_account.save()
    to_account.save()
    accounts = Account.objects.all()
    return render(request,'home.html',{'accounts':accounts})


# def transfer_api(request):
#     from_account_id =  int(request.GET.get('from_account'))
#     to_account_id =  int(request.GET.get('to_account'))
#     transfer_amount = int(request.GET.get('amount'))

#     from_account = Account.objects.get(id=from_account_id)
#     to_account = Account.objects.get(id=to_account_id)

#     from_account.balance = from_account.balance - transfer_amount
#     to_account.balance = to_account.balance + transfer_amount
#     from_account.save()
#     to_account.save()
#     accounts = Account.objects.all()
#     return JsonResponse(request, accounts)

@api_view(['GET'])
def accountlist(request):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def AccountDetail(request, pk):
    account = Account.objects.get(id=pk)
    serializer = AccountSerializer(account,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def AccountCreate(request):
    # n=random.randint(50,500)
    # charsCU = list('ACDEFGHIJKLMNOPQRSTWXYZ')
    # charscs = list('abcdefghijklmnopqrstwxyz')
    # name = ""
    # for x in range(1):
    #     name += random.choice(charsCU)
    # for x in range(10):
    #     name += random.choice(charscs)
    # name += " "
    # for x in range(1):
    #     name += random.choice(charsCU)
    # for x in range(6):
    #     name += random.choice(charscs)
    # data['username'] = name 
    # data['balance'] = n
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    # b = Account(username=name, balance=n)
    # b.save()

    return Response(serializer.data)
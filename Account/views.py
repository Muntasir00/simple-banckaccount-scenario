from django.http import JsonResponse
from django.shortcuts import render
from .models import Account
import random
from Account import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AccountSerializer,transferSerializer,AccountUpdateSerializer
from django.contrib import messages
from rest_framework import status


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
    messages.success(request,"Account created successfully")
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
    messages.success(request,"Balance Transferred successfully")
    accounts = Account.objects.all()
    return render(request,'home.html',{'accounts':accounts})


# def transfer_api(request):
#     from_account_id =  int(request.POST.get('from_account'))
#     to_account_id =  int(request.POST.get('to_account'))
#     transfer_amount = int(request.POST.get('amount'))

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
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def AccountDetail(request, pk):
    account = Account.objects.get(id=pk)
    serializer = AccountSerializer(account,many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)

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
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # b = Account(username=name, balance=n)
    # b.save()

   

@api_view(['POST'])
def transfer_api(request):
    serializer = transferSerializer(data=request.data)
    print(serializer.is_valid())
    print(serializer.errors)
    if serializer.is_valid():
        from_account = Account.objects.get(id=serializer.data["from_account"])
        to_account = Account.objects.get(id=serializer.data["to_account"])
        transfer_amount = int(serializer.data["balance"])

        from_account.balance = from_account.balance - transfer_amount
        to_account.balance = to_account.balance + transfer_amount
        from_account.save()
        to_account.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # accounts = Account.objects.all()
    # return JsonResponse(request, accounts)

@api_view(['PUT'])
def Update_account(request):
    serializer = AccountUpdateSerializer(data=request.data)
    if serializer.is_valid():
        account= Account.objects.get(id=serializer.data["id"])
        account.username = serializer.data["username"]
        account.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


 
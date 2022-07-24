from django.contrib import admin

from Account.models import Account
@admin.register(Account)

class AccountAdmin(admin.ModelAdmin):
    list_display = ['username','balance','freeze_type','hold']
    list_editable = ['freeze_type','hold','balance']

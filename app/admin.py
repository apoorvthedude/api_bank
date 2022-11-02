from django.contrib import admin
from .models import banks,Branches,BankBranches

# Register your models here.
admin.site.register(banks)
admin.site.register(Branches)
admin.site.register(BankBranches)
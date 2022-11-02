from dataclasses import fields
import graphene

from graphene_django import DjangoObjectType,DjangoListField

from .models import banks

class BankDetails(DjangoObjectType):
    class Meta:
        model = banks
        fields = "__all__"

class Query(graphene.ObjectType):
    all_banks = graphene.List(BankDetails)
    branch_details = graphene.Field(BankDetails,bank_id=graphene.Int())

    def resolve_all_banks(self,info,**kwargs):
        return bank.objects.all()
    def resolve_branch_details(self,info,bank_id):
        return bank.objects.get(pk=bank_id)
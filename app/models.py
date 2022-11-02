from tabnanny import verbose
from django.db import models

# Create your models here.

class banks(models.Model):
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    bank_id = models.BigIntegerField(primary_key=True)

    class Meta:
        #verbose_name = "bank"
        db_table = 'banks'

        def __str__(self) -> str:
            return self.name

class Branches(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=50)
    bank = models.ForeignKey(banks, models.CASCADE, blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        #verbose_name = "branch"
        #verbose_name_plural = "branches"
        db_table = 'branches'

    def __str__(self) -> str:
        return f'{self.branch} ({self.bank.name})'

class BankBranches(models.Model):
    ifsc = models.CharField(primary_key=True, max_length=100)
    bank_id = models.BigIntegerField(blank=True, null=True)
    branch = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    bank_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        #verbose_name = "bank branch"
        #verbose_name_plural = "bank branches"
        managed = False
        db_table = 'bank_branches'

    def __str__(self) -> str:
        return f'{self.branch} ({self.bank_name})'
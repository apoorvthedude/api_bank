from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class bank(models.Model):
    ifsc = models.CharField(_("ifsc"),max_length= 100)
    
    bank_name = models.CharField(_("bank_name"),max_length= 250)
    
    bank_id = models.IntegerField(_("bank_id"))
    
    branch = models.CharField(_("branch"),max_length= 100)
    
    state = models.CharField(_("state"),max_length= 100)
    
    district = models.CharField(_("district"),max_length= 100)
    
    city = models.CharField(_("city"),max_length= 100)
    
    address = models.CharField(_("address"),max_length= 100)

    def __str__(self):
        return self.bank_name
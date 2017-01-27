from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from core.models import CreatedModifiedMixin

# Create your models here.# Create your models here.
from django.db import models

class ContactManager():
    
    def postaddress(moniker=None,street=None,municipality=None,region=None,postcode=None,country=None,label=None,type=None,subtype=None,primary=False):
        return {
            'kind':'postal-address',
            
            'moniker':moniker,
            'label':label,
            'type':type,
            'subtype':subtype,
            'primary':primary,
            
            'data1':street,
            'data2':municipality,
            'data3':region,
            'data4':postcode,
            'data5':country
        }
    
    def email(moniker,address,label=None,type=None,subtype=None,primary=False):
        return {
            'kind': 'email',
            'moniker':moniker,
            'label':label,
            'type':type,
            'subtype':subtype,
            'primary':primary,
            
            'data1':address
        }
    
    def telephone(moniker,address,label=None,type=None,subtype=None,primary=False):
        return {
            'kind' : 'telephone',
            'moniker':moniker,
            'label':label,
            'type':type,
            'subtype':subtype,
            'primary':primary,
            'data1':address
        }

class Contact(models.Model, CreatedModifiedMixin):    
    
    moniker = models.CharField(max_length=64,null=True,blank=True) 
    
    kind = models.CharField(max_length=32,null=True,blank=True) 
    label = models.CharField(max_length=64,null=True,blank=True)
    type = models.CharField(max_length=32,null=True,blank=True)
    subtype = models.CharField(max_length=32,null=True,blank=True)
    primary = models.BooleanField(blank=True,default=False)
    
    data1 = models.CharField(max_length=64,null=True,blank=True)
    data2 = models.CharField(max_length=64,null=True,blank=True)
    data3 = models.CharField(max_length=64,null=True,blank=True)
    data4 = models.CharField(max_length=64,null=True,blank=True)
    data5 = models.CharField(max_length=64,null=True,blank=True)
    data6 = models.CharField(max_length=64,null=True,blank=True)
    data7 = models.CharField(max_length=64,null=True,blank=True)
    data8 = models.CharField(max_length=64,null=True,blank=True)
    data9 = models.CharField(max_length=64,null=True,blank=True)
    data10 = models.TextField(blank=True,null=True)
               
    def __unicode__(self):
        return self.kind
    
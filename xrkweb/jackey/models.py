from django.db import models

# Create your models here.

class IP(models.Model):
    hostname=models.CharField(max_length=50, unique=True)
    ip = models.IPAddressField(unique=True)
#    idc = models.CharField(max_length=50, null=True, blank=True)
#   group = models.ManyToManyField(Group, null=True, blank=True)
    port = models.IntegerField(default='22')
    os = models.CharField(max_length=20, default='linux', verbose_name='Operating System')

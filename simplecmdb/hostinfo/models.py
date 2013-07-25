from django.db import models

# Create your models here.

class Host(models.Model):
    """store host information"""
    vendor = models.CharField(max_length=30)
    product = models.CharField(max_length=30)
    sn = models.CharField(max_length=30)
    hostname = models.CharField(max_length=30)
    osbit = models.CharField(max_length=15)
    osver = models.CharField(max_length=30)
    cpumodel = models.CharField(max_length=30)
    cpucores = models.IntegerField(max_length=2)
    cpunum = models.IntegerField(max_length=2)
    memory = models.CharField(max_length=30)
    ipaddr = models.IPAddressField(max_length=15)
    uuid = models.CharField(max_length=30)    

    def __unicode__(self):
        return self.hostname

#class IPaddr(models.Model):
#    ipaddr = models.IPAddressField()
#    host = models.ForeignKey('Host')


class HostGroup(models.Model):
    name = models.CharField(max_length=30)
    members = models.ManyToManyField(Host)

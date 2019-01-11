from django.db import models

# Create your models here.

# tutorial/models.py
class Ticket(models.Model):
    plugin_name = models.CharField(max_length=100, verbose_name='Plugin Name',default='Blank')
    plugin_id = models.CharField(max_length=100, verbose_name='Plugin ID', default='Blank')
    hostname = models.CharField(max_length=100, verbose_name='Hostname',default='Blank')
    ip_address = models.CharField(max_length=100, verbose_name='Ip Address',default='Blank')
    date = models.CharField(max_length=100, verbose_name='Date',default='Blank')
    tool = models.CharField(max_length=100, verbose_name='Tool', default='Blank')
    def __str__(self):
        return self.plugin_name + ' ' + self.date + ' ' + self.hostname 

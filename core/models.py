__author__ = 'Rodrigo.Oliveira'

from django.db import models

# Create your models here.

class Tracker(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    blood_type = models.CharField(max_length=10, null=True, blank=True)
    patent = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    heartbeat = models.IntegerField(null=True, blank=True)
    lat = models.CharField(max_length=200, null=True, blank=True)
    long = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=200, null=True, blank=True)
    active = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='policial')

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'tracker_name'
        verbose_name = 'Tracker - Dados'
        verbose_name_plural = 'Tracker - Dados'


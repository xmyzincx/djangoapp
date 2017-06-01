from __future__ import unicode_literals

from django.db import models

class ElsysSensorData(models.Model):
    deviceID = models.CharField()
    deviceName = models.CharField()
    payload = models.CharField()
    rssi = models.FloatField()
    timestamp = models.DateField(auto_now=True)
    nodeTimestamp = models.DateField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    light = models.FloatField()
    pir = models.FloatField()
    battery = models.FloatField()

    class Meta:
        unique_together = (('DeviceID', 'nodeTimestamp'),)

    def __unicode__(self):
        return unicode(repr(self))

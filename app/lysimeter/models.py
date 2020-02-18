from djongo import models
from djongo.models import *


class DeviceParams(models.Model):
    lysimeter = models.CharField(max_length=10)  # ID - Id lysimeter
    battery = models.CharField(max_length=10)  # SBV - battery voltage
   
    """ AmbientReading """
    ambient_temperature = models.CharField(max_length=10)  # sta - Temperature sensor
    ambient_humidity = models.CharField(max_length=10)  # sha - Humidity sensor
    ambient_light01 = models.CharField(max_length=10)  # sla - Luminosity sensor
    ambient_light02 = models.CharField(max_length=10)  # sla - Luminosity sensor
   
    """ SoilReadings """
    # Soil temperature sensor
    soil_temperature01 = models.CharField(max_length=10)  # STS1 - Soil temperature sensor
    soil_temperature02 = models.CharField(max_length=10)  # STS2 - Soil temperature sensor
    soil_temperature03 = models.CharField(max_length=10)  # STS3 - Soil temperature sensor
    # Soil humidity sensor
    soil_humidity01 = models.CharField(max_length=10)  # SHS1 - Soil humidity sensor
    soil_humidity02 = models.CharField(max_length=10)  # SHS2 - Soil humidity sensor
    soil_humidity03 = models.CharField(max_length=10)  # SHS3 - Soil humidity sensor
   
    """  Weight"""
    lysimeter_weight = models.CharField(max_length=10) # Weight sensor *
    sediment_weight = models.CharField(max_length=10) # Weight sensor *

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Reading: %d - Device Id: %s' % (self.id, self.lysimeter)
    
    class Meta:
        ordering = ('-id', )
        verbose_name = "Lysimeter"
        verbose_name_plural = "Lysimeters"

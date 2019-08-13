from django.db import models

class Sensor(models.Model):
    id_lysimeter = models.CharField(max_length=10)
    environment_temperature = models.CharField(max_length=10)
    ambient_humidity = models.CharField(max_length=10)
    ambient_light = models.CharField(max_length=10)
    ground_temperature01 = models.CharField(max_length=10)
    ground_temperature02 = models.CharField(max_length=10)
    ground_temperature03 = models.CharField(max_length=10)
    soil_humidity01 = models.CharField(max_length=10)
    soil_humidity02 = models.CharField(max_length=10)
    soil_humidity03 = models.CharField(max_length=10)
    lysimeter_weight = models.CharField(max_length=10)
    waste_weight = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id_lysimeter

    class Meta:
        verbose_name = "sensor"
        verbose_name_plural = "sensores"
        order_with_respect_to = 'id_lysimeter'

        
    
        

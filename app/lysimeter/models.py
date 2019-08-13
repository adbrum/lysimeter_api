from djongo import models


class AmbientReading(models.Model):
    ambient_temperature = models.CharField(max_length=10)  # sta - Temperature sensor
    ambient_humidity = models.CharField(max_length=10)  # sha - Humidity sensor
    ambient_light = models.CharField(max_length=10)  # sla - Luminosity sensor
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract = True


class DeviceParams(models.Model):
    lysimeter = models.CharField(max_length=10)  # ID - Id lysimeter
    battery = models.CharField(max_length=10)  # SBV - battery voltage
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract = True


class SoilReadings(models.Model):
    # Soil temperature sensor
    soil_temperature01 = models.CharField(max_length=10)  # STS1 - Soil temperature sensor
    soil_temperature02 = models.CharField(max_length=10)  # STS2 - Soil temperature sensor
    soil_temperature03 = models.CharField(max_length=10)  # STS3 - Soil temperature sensor
    # Soil humidity sensor
    soil_humidity01 = models.CharField(max_length=10)  # SHS1 - Soil humidity sensor
    soil_humidity02 = models.CharField(max_length=10)  # SHS2 - Soil humidity sensor
    soil_humidity03 = models.CharField(max_length=10)  # SHS3 - Soil humidity sensor
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract = True


class Weight(models.Model):
    lysimeter_weight = models.CharField(max_length=10) # Weight sensor *
    sediment_weight = models.CharField(max_length=10) # Weight sensor *


    class Meta:
        abstract = True


class Reading(models.Model):
    timestamp = models.DateTimeField()
    ambient_reading = models.EmbeddedModelField(
        model_container=AmbientReading,
    )
    device_params = models.EmbeddedModelField(
        model_container=DeviceParams,
    )
    soil_readings = models.ArrayModelField(
        model_container=SoilReadings,
    )
    weight = models.EmbeddedModelField(
        model_container=Weight,
    )

    def __str__(self):
        return 'Device Id: %s' % (self.device_params.lysimeter)
    
    class Meta:
        verbose_name = "Lysimeter"
        verbose_name_plural = "Lysimeters"
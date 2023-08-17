from django.db import models


class Star(models.Model):
    """
    Universe Stars endpoint model
    """

    class Meta:
        verbose_name_plural = "Stars"
        db_table = "universe_star"

    star_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    age = models.BigIntegerField()
    luminosity = models.FloatField()
    spectral_class = models.TextField()
    temperature = models.IntegerField()
    radius = models.BigIntegerField()
    solar_system_id = models.IntegerField()
    position_x = models.FloatField()
    position_y = models.FloatField()
    position_z = models.FloatField()

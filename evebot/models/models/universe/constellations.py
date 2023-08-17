from django.db import models


class Constellation(models.Model):
    """
    Universe Constellations endpoint model
    """

    class Meta:
        verbose_name_plural = "Constellations"
        db_table = "universe_constellation"

    constellation_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    region_id = models.IntegerField()
    position_x = models.FloatField()
    position_y = models.FloatField()
    position_z = models.FloatField()
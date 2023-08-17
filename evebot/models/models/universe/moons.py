from django.db import models


class Moon(models.Model):
    """
    Universe Moons endpoint model
    """

    class Meta:
        verbose_name_plural = "Moons"
        db_table = "universe_moon"

    moon_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    system_id = models.IntegerField()
    position_x = models.FloatField()
    position_y = models.FloatField()
    position_z = models.FloatField()

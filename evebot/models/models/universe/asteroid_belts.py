from django.db import models


class AsteroidBelt(models.Model):
    """
    Universe Asteroid Belts endpoint model
    """

    class Meta:
        verbose_name_plural = "Asteroid Belts"
        db_table = "universe_asteroid_belt"

    asteroid_belt_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    system_id = models.IntegerField()
    position_x = models.FloatField()
    position_y = models.FloatField()
    position_z = models.FloatField()

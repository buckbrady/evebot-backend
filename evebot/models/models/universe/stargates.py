from django.db import models


class Stargate(models.Model):
    """
    Universe Stargates endpoint model
    """

    class Meta:
        verbose_name_plural = "Stargates"
        db_table = "universe_stargate"

    stargate_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    system_id = models.IntegerField()
    type_id = models.IntegerField()
    destination_stargate_id = models.IntegerField()
    destination_system_id = models.IntegerField()
    position_x = models.FloatField()
    position_y = models.FloatField()
    position_z = models.FloatField()
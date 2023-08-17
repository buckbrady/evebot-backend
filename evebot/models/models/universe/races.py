from django.db import models


class Race(models.Model):
    """
    Universe Races endpoint model
    """

    class Meta:
        verbose_name_plural = "Races"
        db_table = "universe_race"

    race_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    alliance_id = models.IntegerField()

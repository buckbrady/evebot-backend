from django.db import models


class Faction(models.Model):
    """
    Universe Factions endpoint model
    """

    class Meta:
        verbose_name_plural = "Factions"
        db_table = "universe_faction"

    faction_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    corporation_id = models.IntegerField()
    solar_system_id = models.IntegerField()
    militia_corporation_id = models.IntegerField()
    size_factor = models.FloatField()
    station_count = models.IntegerField()
    station_system_count = models.IntegerField()
    is_unique = models.BooleanField()
    icon_id = models.IntegerField()

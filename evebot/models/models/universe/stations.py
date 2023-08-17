from django.db import models


class Station(models.Model):
    """
    Universe Stations endpoint model
    """

    class Meta:
        verbose_name_plural = "Stations"
        db_table = "universe_station"

    station_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    owner = models.IntegerField()
    system_id = models.IntegerField()
    type_id = models.IntegerField()
    position_x = models.FloatField()
    position_y = models.FloatField()
    position_z = models.FloatField()
    reprocessing_efficiency = models.FloatField()
    reprocessing_stations_take = models.FloatField()
    max_dockable_ship_volume = models.FloatField()
    office_rental_cost = models.FloatField()
    services = models.JSONField()

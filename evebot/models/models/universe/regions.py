from django.db import models


class Region(models.Model):
    """
    Universe Regions endpoint model
    """

    class Meta:
        verbose_name_plural = "Regions"
        db_table = "universe_region"

    region_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()

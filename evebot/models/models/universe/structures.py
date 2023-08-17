from django.db import models


class Structure(models.Model):
    """
    Universe Structures endpoint model
    """

    class Meta:
        verbose_name_plural = "Structures"
        db_table = "universe_structure"

    structure_id = models.BigIntegerField(primary_key=True)
    name = models.TextField()
    owner_id = models.IntegerField()
    solar_system_id = models.IntegerField()
    type_id = models.IntegerField()
    position_x = models.FloatField()
    position_y = models.FloatField()
    position_z = models.FloatField()

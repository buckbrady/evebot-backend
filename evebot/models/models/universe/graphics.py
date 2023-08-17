from django.db import models


class Graphic(models.Model):
    """
    Universe Graphics endpoint model
    """

    class Meta:
        verbose_name_plural = "Graphics"
        db_table = "universe_graphic"

    graphic_id = models.IntegerField(primary_key=True)
    collision_file = models.TextField()
    graphic_file = models.TextField()
    icon_folder = models.TextField()
    sof_dna = models.TextField()
    sof_fation_name = models.TextField()
    sof_hull_name = models.TextField()
    sof_race_name = models.TextField()

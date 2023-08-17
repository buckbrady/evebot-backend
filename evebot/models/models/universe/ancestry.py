from django.db import models


class Ancestry(models.Model):
    """
    Universe Ancestries endpoint model
    """

    class Meta:
        verbose_name_plural = "Ancestries"
        db_table = "universe_ancestry"

    ancestry_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    bloodline_id = models.IntegerField()
    description = models.TextField()
    short_description = models.TextField(null=True)
    icon_id = models.IntegerField(null=True)

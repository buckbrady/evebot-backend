from django.db import models


class Bloodline(models.Model):
    """
    Universe Bloodlines endpoint model
    """

    class Meta:
        verbose_name_plural = "Bloodlines"
        db_table = "universe_bloodline"

    bloodline_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    corporation_id = models.IntegerField()
    race_id = models.IntegerField()
    ship_type_id = models.IntegerField()
    perception = models.IntegerField()
    willpower = models.IntegerField()
    charisma = models.IntegerField()
    memory = models.IntegerField()
    intelligence = models.IntegerField()

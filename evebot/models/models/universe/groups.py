from django.db import models


class Group(models.Model):
    """
    Universe Groups endpoint model
    """

    class Meta:
        verbose_name_plural = "Groups"
        db_table = "universe_group"

    group_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    category_id = models.IntegerField()
    published = models.BooleanField()
    types = models.JSONField()

from django.db import models


class Category(models.Model):
    """
    Universe Categories endpoint model
    """

    class Meta:
        verbose_name_plural = "Categories"
        db_table = "universe_category"

    category_id = models.IntegerField(primary_key=True)
    name = models.TextField()
    published = models.BooleanField()
    groups = models.JSONField()
